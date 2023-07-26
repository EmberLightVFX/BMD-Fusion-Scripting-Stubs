 ----------------------------------------------------------------------------
-- Class Browser 1.3 for DaVinci Resolve/Fusion v16+ (and Fusion v9)
--  roger.magnusson@gmail.com
--
--  v1.3 2022-02-23
--   * New: The "See also" references are now links where possible (not clickable in Fusion 9)
--   * New: The class name and inheritance hierarchy is now shown in a sticky header above the scrollable text area
--   * New: Added links to matching Qt documentation (according to my best guesses) when displaying the UI classes 
--   * New: Option to enable verbose log for debugging
--   * New: Option to always rebuild the cached data file on start (set force_update_file = true)
--   * New: Support for manually added classes and class members (currently, methods are added to the Fairlight, Timeline and Timeline item classes in DaVinci Resolve)
--   * New: Open Script Folder button, for easy access to the code when the script has been installed
--   * New: Hover on a method return type to see if it has been given a descriptive name
--   * Fixed: Tag Maps didn't work in v17+ because the table structure had changed
--   * Fixed: UI issues after Qt was updated to 5.15.2
--
--  v1.2.3 2021-03-18
--   * Fixed: Startup crash in Resolve/Fusion v17.1 caused by class types that are no longer available
--   * Fixed: Classes containing only ignored discovered methods (like _cast) caused properties to be skipped
--   * Fixed: FuPath methods weren't being discovered
--
--  v1.2.2 2020-05-14
--   * Fixed: The Plugins path was incorrect for Fusion on Windows
--
--  v1.2.1 2020-05-13
--   * New: Additional properties discovered automatically
--   * New: Several more files are probed for methods and properties
--   * Fixed: Some PreviewControl classes weren't showing in the nested view
--
--  v1.2 2020-05-10
--   * New: Tag Maps and Enum Maps
--   * New: Additional methods that aren't documented in the help system are now discovered automatically
--   * Fixed: Fusion v9 window layout issue
--   * Fixed: Fusion v9 didn't show property types when available
--   * Fixed: Fusion v9 error when registry entries contained tables, added workaround for dumptostring() bug
--
--  v1.1 2020-04-02
--   * Added support for showing registry entries associated with a class
--
--  v1.0 2020-02-23
--
--   Inspired by Andrew Hazeldens
--    "FusionScript Help Browser" available in the
--    WSL Reactor package manager:
--    https://www.steakunderwater.com/wesuckless/viewtopic.php?f=32&t=3067
--
----------------------------------------------------------------------------


local docsify_location = ""
local pythonDocs = {}

local hide_classes_without_members = true

local json = require("dkjson")

local runtime_version = app:GetVersion()
if (not runtime_version.App) then -- For Fusion 9 compatibility
	runtime_version.App = "Fusion"
end

local function get_path_info(full_path)
	if (full_path ~= nil and #full_path > 0) then
		local path, filename, extension = string.match(full_path, "(.-)([^\\/]-%.?([^%.\\/]*))$")

		return { Path = path, Filename = filename, Extension = extension, FilenameWithoutExtension = filename:match("(.+)%..+"), FullPath = path..filename }
	else
		return {}
	end
end

local ui = app.UIManager
local dispatcher = bmd.UIDispatcher(ui)
local classes = {}
local tag_map = {}
local enum_map = {}
local discovered_class_methods = {}
local discovered_class_properties = {}
local registry_index = {}
local class_type_index = {}
local window = {}
local windowItems = {}
local last_displayed_class = ""
local splash_window = {}
local splash_items = {}
local is_filtered = false
local cell_width = 290
local script_name = "Class Browser 1.3"
local script_file = get_path_info(debug.getinfo(1,"S").source:match("^.*%@(.*)"))


local headerList = {}
--[[
short_help
name
--qt--
	name
	url
--class_inheritance--
	--i--
]]--
local propertiesList = {}
--[[
--i--
	header
	info_text
	--items--
		name
		return_type
		access_class
		short_help
		description
		--see_also--
			-(another_method)
			method
			name
			-(another_property)
			property
			name
			-(another_root)
			name
			-(same_method)
			name
			-(same_property)
			name
			-(unknown)
			name
			-(not_found)
			name
]]--
local methodList = {}
--[[
--i--
	header
	info_text
	--items--
		name
		short_help
		usage
		description
		--see_also--
			-(another_method)
			method
			name
			-(another_property)
			property
			name
			-(another_root)
			name
			-(same_method)
			name
			-(same_property)
			name
			-(unknown)
			name
			-(not_found)
			name
]]--
local tagsList = {}
--[[
(Tag Map)
--i--
	method
	parent_tag
	~tags~
		value
		key_type
		enum_name
		--enum_value--
			--i--
]]--
local registryList = {}
--[[
(Registry Attributes)
--i--
	full_name
	value
	type (?)
]]--


-- Options
local verbose_log = false
local force_update_file = false
local add_class_members = true


-- UI/Qt mapping
local qt_documentation = -- https://doc.qt.io/qt-5.15/classes.html
{
	UIActionStrip = "",
	UIActionTree = "",
	UIButton = { Name = "QPushButton", Url = "https://doc.qt.io/qt-5.15/qpushbutton.html" },
	UICheckBox = { Name = "QCheckBox", Url = "https://doc.qt.io/qt-5.15/qcheckbox.html" },
	UIColorPicker = { Name = "QColorDialog", Url = "https://doc.qt.io/qt-5.15/qcolordialog.html" },
	UIComboBox = { Name = "QComboBox", Url = "https://doc.qt.io/qt-5.15/qcombobox.html" },
	UIDialog = { Name = "QDialog", Url = "https://doc.qt.io/qt-5.15/qdialog.html" },
	UIDoubleSpinBox = { Name = "QDoubleSpinBox", Url = "https://doc.qt.io/qt-5.15/qdoublespinbox.html" },
	UIFont = { Name = "QFont", Url = "https://doc.qt.io/qt-5.15/qfont.html" },
	UIGap = { Name = "QSpacerItem", Url = "https://doc.qt.io/qt-5.15/qspaceritem.html" },
	UIGroup = { Name = "QBoxLayout", Url = "https://doc.qt.io/qt-5.15/qboxlayout.html" },
	UIHGap = { Name = "QSpacerItem", Url = "https://doc.qt.io/qt-5.15/qspaceritem.html" },
	UIHGroup = { Name = "QHBoxLayout", Url = "https://doc.qt.io/qt-5.15/qhboxlayout.html" },
	UIIcon = "",
	UIItem = "",
	UILabel = { Name = "QLabel", Url = "https://doc.qt.io/qt-5.15/qlabel.html" },
	UILineEdit = { Name = "QLineEdit", Url = "https://doc.qt.io/qt-5.15/qlineedit.html" },
	UIManager = "",
	UISlider = { Name = "QSlider", Url = "https://doc.qt.io/qt-5.15/qslider.html" },
	UISpinBox = { Name = "QSpinBox", Url = "https://doc.qt.io/qt-5.15/qspinbox.html" },
	--UIStack = { Name = "QStackedLayout", Url = "https://doc.qt.io/qt-5.15/qstackedlayout.html" }, -- ?
	UIStack = { Name = "QStackedWidget", Url = "https://doc.qt.io/qt-5.15/qstackedwidget.html" }, -- ?
	UITabBar = { Name = "QTabBar", Url = "https://doc.qt.io/qt-5.15/qtabbar.html" },
	UITextEdit = { Name = "QTextEdit", Url = "https://doc.qt.io/qt-5.15/qtextedit.html" },
	UITimer = { Name = "QTimer", Url = "https://doc.qt.io/qt-5.15/qtimer.html" },
	UITree = { Name = "QTreeWidget", Url = "https://doc.qt.io/qt-5.15/qtreewidget.html" },
	UITreeItem = { Name = "QTreeWidgetItem", Url = "https://doc.qt.io/qt-5.15/qtreewidgetitem.html" },
	UIVGap = { Name = "QSpacerItem", Url = "https://doc.qt.io/qt-5.15/qspaceritem.html" },
	UIVGroup = { Name = "QVBoxLayout", Url = "https://doc.qt.io/qt-5.15/qvboxlayout.html" },
	UIWidget = { Name = "QWidget", Url = "https://doc.qt.io/qt-5.15/qwidget.html" },
	UIWindow = { Name = "QWindow", Url = "https://doc.qt.io/qt-5.15/qwindow.html" }
}

-- Some functions are loaded from strings since we need to use them in two different contexts
local split_function = 
[[return function(text, delimiter) -- Splits a string on a delimiter into a table, the delimiter is removed
	local result = {};

	-- Escape all non alphanumeric characters in the delimiter, we need this escaped in the gmatch function below
	local escaped_delimiter = delimiter:gsub("([^%w])", "%%%1")

	for match in (text..delimiter):gmatch("(.-)"..escaped_delimiter) do
		table.insert(result, match)
	end

	return result;
end
]]

local trim_function = 
[[return function(str) -- bmd.trim isn't available in all contexts
	return str:gsub("^%s+", ""):gsub("%s+$", "")
end
]]

local log_function = 
[[return function(str, log_type)
	local print_verbose_log = ]]..tostring(verbose_log)..[[

	if ((log_type == "verbose" and print_verbose_log) or log_type ~= "verbose") then
		print(str)
	end
end
]]

local split = loadstring(split_function)()
local trim = loadstring(trim_function)()
local log = loadstring(log_function)()

-- Members to add manually, can be for existing classes or new classes
local added_class_members = {}

if (add_class_members) then
	added_class_members =
	{
		Classes = 
		{
			GalleryStill = 
			{ 
				ShortHelp = "This class does not provide any API functions but the object type is used by functions in other classes."
			},
		},
		Properties = 
		{
			--ExampleClass = table.pack(
			--	-- Test
			--	{
			--		Name = "Test",
			--		Type = "Variable",
			--		VarRead = true,
			--		VarWrite = true,
			--		ShortHelp = "Short overview",
			--		Usage = table.pack(
			--			{
			--				Returns = table.pack(
			--					{
			--						Type = "boolean",
			--						Name = "success"
			--					}
			--				),
			--				Args = {},
			--				Description = ""
			--			}
			--		),
			--		Description = table.pack(
			--			{
			--				Type = "Body",
			--				Text = "Some description"
			--			}
			--		),
			--		SeeAlso = table.pack(
			--			{
			--				Text = "SomethingElse"
			--			}
			--		)
			--	}
			--)
		},
		Methods =
		{
			-- Proof of concept, added the official documentation to this class
			Resolve = table.pack(
				-- Fusion
				{
					Name = "Fusion",
					Type = "Function",
					ShortHelp = "Returns the Fusion object. Starting point for Fusion scripts.",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "Fusion",
									Name = "Fusion object"
								}
							),
							Args = {},
							Description = ""
						}
					),
					Description = {},
					SeeAlso = {}
				},

				-- GetMediaStorage
				{
					Name = "GetMediaStorage",
					Type = "Function",
					ShortHelp = "Returns the media storage object to query and act on media locations.",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "MediaStorage",
									Name = "MediaStorage object"
								}
							),
							Args = {},
							Description = ""
						}
					),
					Description = {},
					SeeAlso = {}
				},

				-- GetProjectManager
				{
					Name = "GetProjectManager",
					Type = "Function",
					ShortHelp = "Returns the project manager object for currently open database.",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "ProjectManager",
									Name = "ProjectManager object"
								}
							),
							Args = {},
							Description = ""
						}
					),
					Description = {},
					SeeAlso = {}
				},

				-- OpenPage
				{
					Name = "OpenPage",
					Type = "Function",
					ShortHelp = "Switches to indicated page in DaVinci Resolve.",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "success"
								}
							),
							Args = table.pack(
								{
									Type = "string",
									Optional = false,
									Name = "pageName"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "PageName: \"media\"\n          \"cut\"\n          \"edit\"\n          \"fusion\"\n          \"color\"\n          \"fairlight\"\n          \"deliver\"\n\nReturns: true if the operation was successful"
						}
					),
					SeeAlso = {}
				},

				-- GetCurrentPage
				{
					Name = "GetCurrentPage",
					Type = "Function",
					ShortHelp = "Returns the page currently displayed in the main window.",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "string",
									Name = "pageName"
								}
							),
							Args = {},
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "Returns one of: \"media\"\n                \"cut\"\n                \"edit\"\n                \"fusion\"\n                \"color\"\n                \"fairlight\"\n                \"deliver\""
						}
					),
					SeeAlso = {}
				},

				-- GetProductName
				{
					Name = "GetProductName",
					Type = "Function",
					ShortHelp = "Returns product name.",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "string",
									Name = "product name"
								}
							),
							Args = {},
							Description = ""
						}
					),
					Description = {},
					SeeAlso = {}
				},

				-- GetVersion
				{
					Name = "GetVersion",
					Type = "Function",
					ShortHelp = "Returns list of product version fields in [major, minor, patch, build, suffix] format.",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "table",
									Name = "version fields"
								}
							),
							Args = {},
							Description = ""
						}
					),
					Description = {},
					SeeAlso = {}
				},

				-- GetVersionString
				{
					Name = "GetVersionString",
					Type = "Function",
					ShortHelp = "Returns product version in \"major.minor.patch[suffix].build\" format.",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "string",
									Name = "version string"
								}
							),
							Args = {},
							Description = ""
						}
					),
					Description = {},
					SeeAlso = {}
				},

				-- LoadLayoutPreset
				{
					Name = "LoadLayoutPreset",
					Type = "Function",
					ShortHelp = "Loads UI layout from saved preset.",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "success"
								}
							),
							Args = table.pack(
								{
									Type = "string",
									Optional = false,
									Name = "presetName"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "Returns: true if the operation was successful"
						}
					),
					SeeAlso = {}
				},

				-- UpdateLayoutPreset
				{
					Name = "UpdateLayoutPreset",
					Type = "Function",
					ShortHelp = "Overwrites preset with current UI layout.",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "success"
								}
							),
							Args = table.pack(
								{
									Type = "string",
									Optional = false,
									Name = "presetName"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "Returns: true if the operation was successful"
						}
					),
					SeeAlso = {}
				},

				-- ExportLayoutPreset
				{
					Name = "ExportLayoutPreset",
					Type = "Function",
					ShortHelp = "Exports preset named 'presetName' to path 'presetFilePath'.",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "success"
								}
							),
							Args = table.pack(
								{
									Type = "string",
									Optional = false,
									Name = "presetName"
								},
								{
									Type = "string",
									Optional = false,
									Name = "presetFilePath"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "Returns: true if the operation was successful"
						}
					),
					SeeAlso = {}
				},

				-- DeleteLayoutPreset
				{
					Name = "DeleteLayoutPreset",
					Type = "Function",
					ShortHelp = "Deletes preset named 'presetName'.",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "success"
								}
							),
							Args = table.pack(
								{
									Type = "string",
									Optional = false,
									Name = "presetName"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "Returns: true if the operation was successful"
						}
					),
					SeeAlso = {}
				},

				-- SaveLayoutPreset
				{
					Name = "SaveLayoutPreset",
					Type = "Function",
					ShortHelp = "Saves current UI layout as a preset named 'presetName'.",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "success"
								}
							),
							Args = table.pack(
								{
									Type = "string",
									Optional = false,
									Name = "presetName"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "Returns: true if the operation was successful"
						}
					),
					SeeAlso = {}
				},

				-- ImportLayoutPreset
				{
					Name = "ImportLayoutPreset",
					Type = "Function",
					ShortHelp = "Imports preset from path 'presetFilePath'.",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "success"
								}
							),
							Args = table.pack(
								{
									Type = "string",
									Optional = false,
									Name = "presetFilePath"
								},
								{
									Type = "string",
									Optional = true,
									Name = "presetName"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "The optional argument 'presetName' specifies how the preset shall be named. If not specified, the preset is named based on the filename.\n\nReturns: true if the operation was successful"
						}
					),
					SeeAlso = {}
				},

				-- Quit
				{
					Name = "Quit",
					Type = "Function",
					ShortHelp = "Quits the Resolve App.",
					Usage = table.pack(
						{
							Returns = {},
							Args = {},
							Description = ""
						}
					),
					Description = {},
					SeeAlso = {}
				}
			),
			
			-- Deprecated methods are labeled as Deprecated
			--TODO
			ProjectManager = table.pack(
				-- GetProjectsInCurrentFolder [Deprecated]
				{
					Name = "GetProjectsInCurrentFolder",
					Type = "Function",
					ShortHelp = "Deprecated",
					Usage = {},
					Description = {},
					SeeAlso = {},
				},
				
				-- GetFoldersInCurrentFolder [Deprecated]
				{
					Name = "GetFoldersInCurrentFolder",
					Type = "Function",
					ShortHelp = "Deprecated",
					Usage = {},
					Description = {},
					SeeAlso = {},
				}
			),

			-- Deprecated methods are labeled as Deprecated
			--TODO
			Project = table.pack(
				-- GetPresets [Deprecated]
				{
					Name = "GetPresets",
					Type = "Function",
					ShortHelp = "Deprecated",
					Usage = {},
					Description = {},
					SeeAlso = {},
				},

				-- GetRenderJobs [Deprecated]
				{
					Name = "GetRenderJobs",
					Type = "Function",
					ShortHelp = "Deprecated",
					Usage = {},
					Description = {},
					SeeAlso = {}
				},

				-- GetRenderPresets [Deprecated]
				{
					Name = "GetRenderPresets",
					Type = "Function",
					ShortHelp = "Deprecated",
					Usage = {},
					Description = {},
					SeeAlso = {}
				}
			),

			-- Deprecated methods are labeled as Deprecated
			--TODO
			MediaStorage = table.pack(
				-- GetMountedVolumes [Deprecated]
				{
					Name = "GetMountedVolumes",
					Type = "Function",
					ShortHelp = "Deprecated",
					Usage = {},
					Description = {},
					SeeAlso = {},
				},
				
				-- GetSubFolders [Deprecated]
				{
					Name = "GetSubFolders",
					Type = "Function",
					ShortHelp = "Deprecated",
					Usage = {},
					Description = {},
					SeeAlso = {},
				},

				-- GetFiles [Deprecated]
				{
					Name = "GetFiles",
					Type = "Function",
					ShortHelp = "Deprecated",
					Usage = {},
					Description = {},
					SeeAlso = {},
				},
				
				-- AddItemsToMediaPool [Deprecated]
				{
					Name = "AddItemsToMediaPool",
					Type = "Function",
					ShortHelp = "Deprecated",
					Usage = {},
					Description = {},
					SeeAlso = {},
				}
			),

			--TODO
			MediaPool = {},

			-- Deprecated methods are labeled as Deprecated
			--TODO
			Folder = table.pack(
				-- GetClips [Deprecated]
				{
					Name = "GetClips",
					Type = "Function",
					ShortHelp = "Deprecated",
					Usage = {},
					Description = {},
					SeeAlso = {},
				},

				-- GetSubFolders [Deprecated]
				{
					Name = "GetSubFolders",
					Type = "Function",
					ShortHelp = "Deprecated",
					Usage = {},
					Description = {},
					SeeAlso = {}
				}
			),

			--TODO
			["Media pool item"] = table.pack(
				-- GetFlags [Deprecated]
				{
					Name = "GetFlags",
					Type = "Function",
					ShortHelp = "Deprecated",
					Usage = {},
					Description = {},
					SeeAlso = {},
				}
			),

			-- Undocumented methods
			-- Deprecated methods are labeled as Deprecated
			--TODO
			Timeline = table.pack(
				-- AddTrack
				{
					Name = "AddTrack",
					Type = "Function",
					ShortHelp = "Adds a track of the given type to the timeline",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "success"
								}
							),
							Args = table.pack(
								{
									Type = "string",
									Optional = false,
									Name = "trackType"
								},
								{
									Type = "string",
									Optional = true,
									Name = "audioTrackType"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "TrackType: \"audio\"\n           \"video\"\n           \"subtitle\"\n\nAudioTrackType: \"mono\"\n                \"stereo\"\n                \"5.1film\"\n                \"7.1film\"\n                \"adaptive\"\n\nReturns: true if the operation was successful"
						}
					),
					SeeAlso = {}
				},

				-- DeleteTrack
				{
					Name = "DeleteTrack",
					Type = "Function",
					ShortHelp = "Deletes a track of the given type at the specified index",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "success"
								}
							),
							Args = table.pack(
								{
									Type = "string",
									Optional = false,
									Name = "trackType"
								},
								{
									Type = "int",
									Optional = false,
									Name = "index"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "TrackType: \"audio\"\n           \"video\"\n           \"subtitle\"\n\nIndex is 1 to GetTrackCount(trackType)\n\nReturns: true if the operation was successful"
						}
					),
					SeeAlso = {}
				},

				-- GetIsTrackEnabled
				{
					Name = "GetIsTrackEnabled",
					Type = "Function",
					ShortHelp = "Returns whether a track is enabled or not",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "enabled"
								}
							),
							Args = table.pack(
								{
									Type = "string",
									Optional = false,
									Name = "trackType"
								},
								{
									Type = "int",
									Optional = false,
									Name = "index"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "TrackType: \"audio\"\n           \"video\"\n           \"subtitle\"\n\nIndex is 1 to GetTrackCount(trackType)"
						}
					),
					SeeAlso = {}
				},

				-- GetIsTrackLocked
				{
					Name = "GetIsTrackLocked",
					Type = "Function",
					ShortHelp = "Returns whether a track is locked or not",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "locked"
								}
							),
							Args = table.pack(
								{
									Type = "string",
									Optional = false,
									Name = "trackType"
								},
								{
									Type = "int",
									Optional = false,
									Name = "index"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "TrackType: \"audio\"\n           \"video\"\n           \"subtitle\"\n\nIndex is 1 to GetTrackCount(trackType)"
						}
					),
					SeeAlso = {}
				},

				-- SetClipsLinked
				{
					Name = "SetClipsLinked",
					Type = "Function",
					ShortHelp = "Links or unlinks the given clips",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "success"
								}
							),
							Args = table.pack(
								{
									Type = "table",
									Optional = false,
									Name = "timelineItems"
								},
								{
									Type = "boolean",
									Optional = false,
									Name = "link"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "Returns: true if the operation was successful"
						}
					),
					SeeAlso = {},
				},

				-- SetTrackEnable
				{
					Name = "SetTrackEnable",
					Type = "Function",
					ShortHelp = "Enables or disables the given track",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "success"
								}
							),
							Args = table.pack(
								{
									Type = "string",
									Optional = false,
									Name = "trackType"
								},
								{
									Type = "int",
									Optional = false,
									Name = "index"
								},
								{
									Type = "boolean",
									Optional = false,
									Name = "enable"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "TrackType: \"audio\"\n           \"video\"\n           \"subtitle\"\n\nIndex is 1 to GetTrackCount(trackType)\n\nReturns: true if the operation was successful"
						}
					),
					SeeAlso = {}
				},

				-- SetTrackLock
				{
					Name = "SetTrackLock",
					Type = "Function",
					ShortHelp = "Locks or unlocks the given track",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "success"
								}
							),
							Args = table.pack(
								{
									Type = "string",
									Optional = false,
									Name = "trackType"
								},
								{
									Type = "int",
									Optional = false,
									Name = "index"
								},
								{
									Type = "boolean",
									Optional = false,
									Name = "lock"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "TrackType: \"audio\"\n           \"video\"\n           \"subtitle\"\n\nIndex is 1 to GetTrackCount(trackType)\n\nReturns: true if the operation was successful"
						}
					),
					SeeAlso = {}
				},

				-- GetItemsInTrack [Deprecated]
				{
					Name = "GetItemsInTrack",
					Type = "Function",
					ShortHelp = "Deprecated",
					Usage = {},
					Description = {},
					SeeAlso = {},
				}
			),

			-- Undocumented methods
			-- Deprecated methods are labeled as Deprecated
			--TODO
			["Timeline item"] = table.pack(
				-- GetClipEnabled
				{
					Name = "GetClipEnabled",
					Type = "Function",
					ShortHelp = "Returns whether a clip is enabled or not",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "enabled"
								}
							),
							Args = {},
							Description = ""
						}
					),
					Description = {},
					SeeAlso = {}
				},

				-- SetClipEnabled
				{
					Name = "SetClipEnabled",
					Type = "Function",
					ShortHelp = "Enables or disables a clip",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "success"
								}
							),
							Args = table.pack(
								{
									Type = "boolean",
									Optional = false,
									Name = "enable"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "Returns: success - true if the action was performed"
						}
					),
					SeeAlso = {}
				},

				-- SetNodeLocked
				{
					Name = "SetNodeLocked",
					Type = "Function",
					ShortHelp = "Locks or unlocks a Color page node at the given nodeIndex",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "success"
								}
							),
							Args = table.pack(
								{
									Type = "int",
									Optional = false,
									Name = "nodeIndex"
								},
								{
									Type = "boolean",
									Optional = false,
									Name = "lock"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "Returns: success - true if the action was performed"
						}
					),
					SeeAlso = {}
				},

				-- GetFusionCompNames [Deprecated]
				{
					Name = "GetFusionCompNames",
					Type = "Function",
					ShortHelp = "Deprecated",
					Usage = {},
					Description = {},
					SeeAlso = {},
				},

				-- GetFlags [Deprecated]
				{
					Name = "GetFlags",
					Type = "Function",
					ShortHelp = "Deprecated",
					Usage = {},
					Description = {},
					SeeAlso = {},
				},

				-- GetVersionNames [Deprecated]
				{
					Name = "GetVersionNames",
					Type = "Function",
					ShortHelp = "Deprecated",
					Usage = {},
					Description = {},
					SeeAlso = {},
				}
			),

			--TODO
			Gallery = {},

			--TODO
			GalleryStillAlbum = {},

			GalleryStill = {},

			-- Method documententation that was available in Resolve v16, but removed in v17
			Fairlight = table.pack(
				-- DoAction
				{
					Name = "DoAction",
					Type = "Function",
					ShortHelp = "Does a Fairlight action",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "success"
								}
							),
							Args = table.pack(
								{
									Type = "string",
									Optional = false,
									Name = "action"
								},
								{
									Type = "string",
									Optional = true,
									Name = "param1"
								},
								{
									Type = "string",
									Optional = true,
									Name = "param2"
								},
								{
									Type = "string",
									Optional = true,
									Name = "param3"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "Arguments: action - name of action to perform (string)\n           param1 - (optional) parameter for action (string or int)\n           param2 - (optional) parameter for action (string or int)\n           param3 - (optional) parameter for action (string or int)\n\nReturns: success - true if the action was performed"
						}
					),
					SeeAlso = {}
				},

				-- GetModuleList
				{
					Name = "GetModuleList",
					Type = "Function",
					ShortHelp = "Returns a table of available modules",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "table",
									Name = "result"
								}
							),
							Args = {},
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "Returns: table of available modules"
						}
					),
					SeeAlso = {}
				},

				-- GetParameter
				{
					Name = "GetParameter",
					Type = "Function",
					ShortHelp = "Returns a specified parameter",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "int",
									Name = "result"
								}
							),
							Args = table.pack(
								{
									Type = "string",
									Optional = false,
									Name = "moduleID"
								},
								{
									Type = "int",
									Optional = false,
									Name = "moduleIndex"
								},
								{
									Type = "string",
									Optional = false,
									Name = "parameterID"
								},
								{
									Type = "int",
									Optional = true,
									Name = "targetModifier"
								},
								{
									Type = "boolean",
									Optional = true,
									Name = "quiet"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "Arguments: moduleID    - Module Type\n           moduleIndex - index of module\n           parameterID - Parameter Identifier\n           targetModifier - (optional)\n           quiet       - (optional)\n\nReturns: integer or text parameter result"
						}
					),
					SeeAlso = {}
				},

				-- GetParameterList
				{
					Name = "GetParameterList",
					Type = "Function",
					ShortHelp = "Returns a table of available parameters",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "table",
									Name = "result"
								}
							),
							Args = {},
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "Returns: table of parameter attributes"
						}
					),
					SeeAlso = {}
				},

				-- SetParameter
				{
					Name = "SetParameter",
					Type = "Function",
					ShortHelp = "Sets a specified parameter",
					Usage = table.pack(
						{
							Returns = table.pack(
								{
									Type = "boolean",
									Name = "success"
								}
							),
							Args = table.pack(
								{
									Type = "string",
									Optional = false,
									Name = "moduleID"
								},
								{
									Type = "int",
									Optional = false,
									Name = "moduleIndex"
								},
								{
									Type = "string",
									Optional = false,
									Name = "parameterID"
								},
								{
									Type = "int",
									Optional = false,
									Name = "value"
								},
								{
									Type = "int",
									Optional = true,
									Name = "targetModifier"
								}
							),
							Description = ""
						}
					),
					Description = table.pack(
						{
							Type = "Body",
							Text = "Arguments: moduleID    - Module Type\n           moduleIndex - index of module\n           parameterID - Parameter Identifier\n           value       - Parameter value (integer or text)\n           targetModifier - (optional)\n\nReturns: boolean true if success"
						}
					),
					SeeAlso = {}
				}
			)
		}
	}
end

-- Removes manually added class members if they should not be visible in the version of Resolve/Fusion that this script is running in
local function trim_added_members(version, members_collection)
	function get_table_length(tbl)
		local table_length = 0
		
		if (tbl) then
			for _, __ in pairs(tbl) do
				table_length = table_length + 1
			end
		end
		
		return table_length
	end

	local function trim_empty_classes(members)
		if (members) then
			for member_name, member_info in pairs(members) do
				if (get_table_length(member_info) == 0) then
					members[member_name] = nil
					log("Trimmed empty manually added class: "..member_name, "verbose")
				end
			end
		end
	end

	if (version.App == "Fusion" or version[1] < 17) then
		members_collection.Methods.Fairlight = nil
		members_collection.Methods.Project = nil
	end

	if (version.App == "Fusion" or version[1] < 16) then
		members_collection.Methods.Timeline = nil
		members_collection.Methods["Timeline item"] = nil
	end

	if (version.App == "Fusion") then
		members_collection.Methods.Resolve = nil
	end

	trim_empty_classes(members_collection.Classes)
	trim_empty_classes(members_collection.Properties)
	trim_empty_classes(members_collection.Methods)
end

trim_added_members(runtime_version, added_class_members)

-- Gets integer values for all known class type constants
for _, class_type in pairs(
	{
		"CT_Any", "CT_Operator", "CT_Tool", "CT_SourceTool", "CT_SinkTool",
		"CT_MergeTool", "CT_Modifier", "CT_Mask", "CT_Spline", "CT_Parameter",
		"CT_ImageFormat", "CT_View", "CT_GLViewer", "CT_InputControl",
		"CT_PreviewControl", "CT_Preview", "CT_BinItem", "CT_ExternalControl",
		"CT_Converter", "CT_3D", "CT_3DFilter", "CT_3DFilterSource", "CT_Event",
		"CT_EventControl", "CT_Protocol", "CT_Utility", "CT_PaintTool",
		"CT_BrushShape", "CT_BrushMode", "CT_ApplyMode", "CT_AnimSegment",
		"CT_FlowType", "CT_Locale", "CT_PreviewMedia", "CT_LayoutItem",
		"CT_Transition", "CT_ToolViewInfo", "CT_ParticleStyle", "CT_ParticleTool",
		"CT_ParticleMergeTool", "CT_ParticleSource", "CT_Region3D",
		"CT_LightData3D", "CT_Light3D", "CT_MtlData3D", "CT_MtlParticle3D",
		"CT_MtlInputs3D", "CT_CameraData3D", "CT_Camera3D", "CT_CurveData3D",
		"CT_Curve3D", "CT_SurfaceData3D", "CT_SurfaceInputs3D", "CT_Renderer3D",
		"CT_RendererInputs3D", "CT_RenderContext3D", "CT_Shader3D",
		"CT_FileFormat3D", "CT_ShadowClass3D", "CT_GLTexture", "CT_MtlSW3D",
		"CT_MtlHW3D", "CT_MtlGL3D", "CT_LightSW3D", "CT_LightHW3D", "CT_LightGL3D", "CT_FuMenu",
		"CT_ConsoleUtility", "CT_ViewLUTPlugin", "CT_UserControl", "CT_LUTFormat", "CT_Prefs"
	}) do
	
	-- Additional constants for future use:
	--"TIME_UNDEFINED",
	--"CLSID_DataType_Audio", "CLSID_DataType_Clip", "CLSID_DataType_Gradient",
	--"CLSID_DataType_Image", "CLSID_DataType_Histogram", "CLSID_DataType_LookUpTable",
	--"CLSID_DataType_Mask", "CLSID_DataType_Number", "CLSID_DataType_Point", "CLSID_DataType_Text",
	--"CLSID_DataType_Polyline", "CLSID_DataType_BSplinePolyline", "CLSID_DataType_TransformMatrix",
	--"CLSID_DataType_Mesh", "CLSID_DataType_Particles", "CLSID_DataType_3D", "CLSID_DataType_FuID",
	--"CLSID_DataType_ScriptVal",
	--"CLSID_View_GL", "CLSID_View_Controls", "CLSID_View_Modifiers", "CLSID_View_Flow",
	--"CLSID_View_SplineEditor", "CLSID_View_Timeline", "CLSID_View_Console", "CLSID_View_Transport",
	--"TC_PRF_Frame", "TC_PRF_SMPTE", "TC_PRF_Feet",
	--"DCMSG_TIMECODE_CHANGED", "DCMSG_LOOKPACK_CHANGED", "DCMSG_PREFS_CHANGED"
	
	-- Some class types are no longer available in v17.1, we'll only use the ones that can be found
	if (app[class_type]) then
		class_type_index[app[class_type]] = class_type
	end
end

-- The attribute descriptions are from the Fusion 8 Scripting Guide:
-- https://documents.blackmagicdesign.com/UserManuals/Fusion8_Scripting_Guide.pdf
-- We'll use these as tooltips when listing attributes
local registry_attribute_descriptions =
{
	REGS_Name = "Specifies the full name of the class represented by this registry entry.",
	REGS_ScriptName = "Specifies the scripting name of the class represented by this registry entry.\nIf not specified, the full name defined by REGS_Name is used.",
	REGS_HelpFile = "The help file and ID for the class.",
	REGI_HelpID = "The help file and ID for the class.",
	REGS_HelpTopic = "The help file and ID for the class.", -- Was REGI_HelpTopicID in the Scripting Guide
	REGS_OpIconString = "Specifies the toolbar icon text used to represent the class.",
	REGS_OpDescription = "Specifies a description of the class.",
	REGS_OpToolTip = "Specifies a tooltip for the class to provide a longer name or description.",
	REGS_Category = "Specifies the category for the class, defining a position in the Tools menu for tool classes.",
	REGI_ClassType = "Specifies the type of this class, based on the classtype constants.",
	REGI_ClassType2 = "Specifies the type of this class, based on the classtype constants.",
	REGS_ID = "A unique ID for this class.", -- Was REGI_ID in the Scripting Guide
	REGI_OpIcon = "A resource ID for a bitmap to be used for toolbar images for this class.", -- Was REGI_OpIconID in the Scripting Guide
	REGS_IconID = "A resource ID for a bitmap to be used for toolbar images for this class.", -- Was REGI_OpIconID in the Scripting Guide
	REGB_OpNoMask = "Indicates if this Tool class cannot deal with being masked.",
	REGI_DataType = "table Specifies a data type RegID dealt with by this class.",
	REGI_TileID = "Specifies a resource ID used for the tile image by this class.",
	REGB_CreateStaticPreview = "Indicates that a preview object is to be created at startup of this type.",
	REGB_CreateFramePreview = "Indicates that a preview object is to be created for each new frame window.",
	REGB_Preview_CanDisplayImage = "Defines various capabilities of a preview class.",
	REGB_Preview_CanCreateAnim = "Defines various capabilities of a preview class.",
	REGB_Preview_CanPlayAnim = "Defines various capabilities of a preview class.",
	REGB_Preview_CanSaveImage = "Defines various capabilities of a preview class.",
	REGB_Preview_CanSaveAnim = "Defines various capabilities of a preview class.",
	REGB_Preview_CanCopyImage = "Defines various capabilities of a preview class.",
	REGB_Preview_CanCopyAnim = "Defines various capabilities of a preview class.",
	REGB_Preview_CanRecord = "Defines various capabilities of a preview class.",
	REGB_Preview_UsesFilenames = "Defines various capabilities of a preview class.",
	REGB_Preview_CanNetRender = "Defines various capabilities of a preview class.",
	REGI_Version = "Defines the version number of this class or plugin.",
	REGI_PI_DataSize = "Defines a custom data size for AEPlugin classes.",
	REGB_Unpredictable = "Indicates if this tool class is predictable or not. Predictable tools will\ngenerate the same result given the same set of input values, regardless of time.",
	REGI_InputDataType = "Specifies a data type RegID dealt with by the main inputs of this class.",
	REGB_OperatorControl = "Indicates if this tool class provides custom overlay control handling.",
	REGB_Source_GlobalCtrls = "Indicates if this source tool class has global range controls.",
	REGB_Source_SizeCtrls = "Indicates if this source tool class has image resolution controls.",
	REGB_Source_AspectCtrls = "Indicates if this source tool class has image aspect controls.",
	REGB_NoAutoProxy = "Indicates if this tool class does not want things to be autoproxied when it is adjusted.",
	REGI_Logo = "Specifies a resource ID of a company logo for this class.",
	REGI_Priority = "Specifies the priority of this class on the registry list.",
	REGB_NoBlendCtrls = "Indicates if this tool class does not have blend controls.",
	REGB_NoObjMatCtrls = "Indicates if this tool class does not have Object/Material selection controls.",
	REGB_NoMotionBlurCtrls = "Indicates if this tool class does not have Motion Blur controls.",
	REGB_NoAuxChannels = "Indicates if this tool class cannot deal with being given Auxiliary channels (such as Z, ObjID, etc)",
	REGB_EightBitOnly = "Indicates if this tool class cannot deal with being given greater than 8 bit per channel images.",
	REGB_ControlView = "Indicates if this class is a control view class.",
	REGB_NoSplineAnimation = "Specifies that this data type (parameter class) cannot be animated using a spline.",
	REGI_MergeDataType = "Specifies what type of data this merge tool class is capable of merging.",
	REGB_ForceCommonCtrls = "Forces the tool to have common controls like motion blur, blend etc, even on modifiers.",
	REGB_Particle_ProbabilityCtrls = "Specifies that particle tools should have (or not have) various standard sets of controls.",
	REGB_Particle_SetCtrls = "Specifies that particle tools should have (or not have) various standard sets of controls.",
	REGB_Particle_AgeRangeCtrls = "Specifies that particle tools should have (or not have) various standard sets of controls.",
	REGB_Particle_RegionCtrls = "Specifies that particle tools should have (or not have) various standard sets of controls.",
	REGB_Particle_RegionModeCtrls = "Specifies that particle tools should have (or not have) various standard sets of controls.",
	REGB_Particle_StyleCtrls = "Specifies that particle tools should have (or not have) various standard sets of controls.",
	REGB_Particle_EmitterCtrls = "Specifies that particle tools should have (or not have) various standard sets of controls.",
	REGB_Particle_RandomSeedCtrls = "Specifies that particle tools should have (or not have) various standard sets of controls.",
	REGI_Particle_DefaultRegion = "Specifies the RegID of a default Region for this particle tool class.",
	REGI_Particle_DefaultStyle = "Specifies the RegID of a default Style for this particle tool class.",
	REGI_MediaFormat_Priority = "Specifies the priority of a media format class.",
	REGS_MediaFormat_FormatName = "Specifies the name of a media format class",
	REGST_MediaFormat_Extension = "Specifies the extensions supported by a media format class",
	REGB_MediaFormat_CanLoad = "Specify various capabilities of a media format class",
	REGB_MediaFormat_CanSave = "Specify various capabilities of a media format class",
	REGB_MediaFormat_CanLoadMulti = "Specify various capabilities of a media format class",
	REGB_MediaFormat_CanSaveMulti = "Specify various capabilities of a media format class",
	REGB_MediaFormat_WantsIOClass = "Specify various capabilities of a media format class",
	REGB_MediaFormat_LoadLinearOnly = "Specify various capabilities of a media format class",
	REGB_MediaFormat_SaveLinearOnly = "Specify various capabilities of a media format class",
	REGB_MediaFormat_CanSaveCompressed = "Specify various capabilities of a media format class",
	REGB_MediaFormat_OneShotLoad = "Specify various capabilities of a media format class",
	REGB_MediaFormat_OneShotSave = "Specify various capabilities of a media format class",
	REGB_MediaFormat_CanLoadImages = "Specify various capabilities of a media format class",
	REGB_MediaFormat_CanSaveImages = "Specify various capabilities of a media format class",
	REGB_MediaFormat_CanLoadAudio = "Specify various capabilities of a media format class",
	REGB_MediaFormat_CanSaveAudio = "Specify various capabilities of a media format class",
	REGB_MediaFormat_CanLoadText = "Specify various capabilities of a media format class",
	REGB_MediaFormat_CanSaveText = "Specify various capabilities of a media format class",
	REGB_MediaFormat_CanLoadMIDI = "Specify various capabilities of a media format class",
	REGB_MediaFormat_CanSaveMIDI = "Specify various capabilities of a media format class",
	REGB_MediaFormat_ClipSpecificInputValues = "Specify various capabilities of a media format class",
	REGB_MediaFormat_WantsUnbufferedIOClass = "Specify various capabilities of a media format class",
	REGB_ImageFormat_CanLoadFields = "Specify various capabilities of an image format class",
	REGB_ImageFormat_CanSaveField = "Specify various capabilities of an image format class",
	REGB_ImageFormat_CanScale = "Specify various capabilities of an image format class",
	REGB_ImageFormat_CanSave8bit = "Specify various capabilities of an image format class",
	REGB_ImageFormat_CanSave24bit = "Specify various capabilities of an image format class",
	REGB_ImageFormat_CanSave32bit = "Specify various capabilities of an image format class",
}

function clean(inputString)
    -- Define a pattern to match all non-printable and non-ASCII characters
    local pattern = "[^%w%p%s]"

    -- Use the pattern to replace all matches with an empty string
    local cleanedString = inputString:gsub(pattern, '')

    return cleanedString
end

-- Counts the occurrences of the given pattern in a string
local function count(text, pattern)
	return select(2, text:gsub(pattern, ""))
end

-- Gets the help information for all classes
local function get_classes()
	local classes = {}
	
	for i, class_name in ipairs(app:GetHelpRaw()) do
		local help = app:GetHelpRaw(class_name)

		-- Store with numerical id
		classes[i] =
		{
			name = class_name,
			path = "",
			parent = help.Parent,
			has_members = #help.Members > 0
		}

		-- Store a reference with class name as id that we can
		-- use for fast lookup
		local existing_class = classes[class_name]
		if (existing_class) then
			--log("Duplicate class name found: "..class_name)
			-- Duplicates don't matter in practice since GetHelpRaw
			-- doesn't seem to be able to tell them apart anyway
			-- (they have the same inheritance path)
		else
			classes[class_name] = classes[i]
		end
	end
	
	-- Get full inheritance path of each class
	for i, class in ipairs(classes) do
		local stack = table.pack(class)
		local current_path = ""
	
		-- Build the path by following each parent
		while (#stack > 0) do
			local current_class = table.remove(stack)
	
			current_path = "/"..current_class.name..current_path
	
			local parent_class = current_class.parent
	
			if (parent_class) then
				table.insert(stack, classes[parent_class])
			end
		end
	
		class.path = current_path
	end
	
	return classes
end

-- Gets registry attributes for all classes
local function get_registry()
	local registry = {}

	for _, reg in ipairs(app:GetRegList()) do
		if (reg) then
			local reg_attr = reg:GetAttrs()

			if (reg_attr) then
				if (registry[reg_attr.REGS_ID]) then
					--log("Duplicate entry: "..reg_attr.REGS_ID)
				else
					registry[reg_attr.REGS_ID] = reg_attr
				end
			end
		end
	end

	return registry
end

-- Loads TagMap and EnumMap from another context, tries to discover additional methods in the fusionsystem linked library
local function load_maps(version)
	local fusion_path

	if (version.App == "Resolve" or version[1] >= 16) then
		fusion_path = app:MapPath("FusionLibs:")
	else
		-- Fusion 9
		fusion_path = app:MapPath("Fusion:")
	end

	local temp_folder

	if (ffi.os == "Windows") then
		temp_folder = os.getenv("TEMP").."\\"
	else
		temp_folder = os.getenv("TMPDIR")

		if (ffi.os == "Linux" and not temp_folder) then
			temp_folder = "/tmp/"
		end
	end

	local plugins_folder = "Plugins"

	if (version.App == "Fusion" and ffi.os == "Windows") then
		plugins_folder = plugins_folder..[[\Blackmagic]]
	end

	local data_filename = temp_folder..version.App.."_Class_Browser.luatable"
	local data

	local function update_file(filename)
		-- Declare a sleep function available in the OS (we can't use Fusion():Sleep() because it sleeps the thread we want to wait for)
		ffi.cdef[[ void Sleep(int ms); int poll(struct pollfd *fds,unsigned long nfds,int timeout); ]]
		local sleep = iif(ffi.os == "Windows", function(milliseconds) ffi.C.Sleep(milliseconds) end, function(milliseconds) ffi.C.poll(nil,0,milliseconds) end)

		if (bmd.fileexists(filename)) then
			assert(os.remove(filename))
		end
		
		-- Get the data in a context where EnumMap, TagMap and functions aren't limited as they are when used in scripts after Fusion ~8
		app:Execute(
		[===[
			local fusion_filenames = table.pack
			(
				{
					Windows = "fusionsystem.dll",
					OSX = "libfusionsystem.dylib",
					Linux = "libfusionsystem.so",
				},
				{
					Windows = "fusionoperators.dll",
					OSX = "libfusionoperators.dylib",
					Linux = "libfusionoperators.so",
				},
				{
					Windows = "fusioncontrols.dll",
					OSX = "libfusioncontrols.dylib",
					Linux = "libfusioncontrols.so",
				},
				{
					Windows = "fusionscript.dll",
					OSX = "fusionscript.so",
					Linux = "fusionscript.so",
				},
				{
					Windows = [[]===]..plugins_folder..[===[\fuses.plugin]],
					OSX = [[]===]..plugins_folder..[===[/fuses.plugin]],
					Linux = [[]===]..plugins_folder..[===[/fuses.plugin]],
				},
				{
					Windows = [[]===]..plugins_folder..[===[\text.plugin]],
					OSX = [[]===]..plugins_folder..[===[/text.plugin]],
					Linux = [[]===]..plugins_folder..[===[/text.plugin]],
				}
			)

			for i = 1, fusion_filenames.n do
				fusion_filenames[i].Windows = [[]===]..fusion_path..[===[]]..fusion_filenames[i].Windows
				fusion_filenames[i].OSX = [[]===]..fusion_path..[===[]]..fusion_filenames[i].OSX
				fusion_filenames[i].Linux = [[]===]..fusion_path..[===[]]..fusion_filenames[i].Linux
			end

			local ffi_prefix = " ffi_"
			local split = loadstring([[]===]..split_function..[===[]])()
			local trim = loadstring([[]===]..trim_function..[===[]])()
			local log = loadstring([[]===]..log_function..[===[]])()

			local function find_rev(str, findstr)
				local current_index = -1
				local last_index

				repeat
					last_index = current_index
					current_index = str:find(findstr, current_index + 1, true)
				until (current_index == nil)
				
				return last_index
			end

			local function get_fusionsystem_content(fusionsystem)
				if (bmd.fileexists(fusionsystem)) then
					local file_handle = assert(io.open(fusionsystem, "rb"))
					local fusionsystem_content = file_handle:read("*all")
					assert(file_handle:close())

					local ffi_str = "ffi_" -- Not the same as ffi_prefix
				
					local first_ffi_index = fusionsystem_content:find(ffi_str, 1, true)
					fusionsystem_content = fusionsystem_content:sub(first_ffi_index)
				
					local last_ffi_index = find_rev(fusionsystem_content, "\0"..ffi_str)
					fusionsystem_content = fusionsystem_content:sub(1, last_ffi_index)

					log(string.format("Loaded library: \"%s\"", fusionsystem), "verbose")

					return { ffi_data = fusionsystem_content } -- Making this a table we can pass by reference between functions
				else
					log(string.format("Specified file not found: \"%s\"", fusionsystem), "verbose")

					return { ffi_data = '' }
				end
			end

			local function get_member_definition(fusionsystem_content, current_position)
				local start_position_found

				repeat
					local current_character = fusionsystem_content.ffi_data:sub(current_position - 1, current_position - 1)
							
					if (current_character) then
						if (current_character == "\0") then
							start_position_found = true
						else
							current_position = current_position - 1
						end
					else
						break
					end
				until (start_position_found)

				return fusionsystem_content.ffi_data:sub(current_position, fusionsystem_content.ffi_data:find(")", current_position, true))
			end

			local function convert_numeric_types(type_name)
				-- I prefer seeing the original types, but if you want to convert every parameter/return type to the native Lua "number", uncomment these lines
				
				--if (type_name == "uint8" or type_name == "uint16" or type_name == "uint" or type_name == "uint32" or type_name == "uint64") then
				--	return "number"
				--	--return "number (unsigned int)"
				--elseif (type_name == "int8" or type_name == "int16" or type_name == "int" or type_name == "int32" or type_name == "int64") then
				--	return "number"
				--	--return "number (signed int)"
				--elseif (type_name == "float16" or type_name == "float" or type_name == "float32" or type_name == "float64") then
				--	return "number"
				--	--return "number (float)"
				--else
					return type_name
				--end
			end

			local function parse_member_definition(member_definition, member_type, split_on)
				local member_help =
				{
					Type = member_type,
					Definition = member_definition,
					Usage =
					{
						[1] = 
						{
							Returns = {},
							Args = {},
							Description = ""
						}
					},
					LongHelp = "",
					SeeAlso = {},
					ShortHelp = "",
					Description = {},
				}
				
				if (member_type == "Variable") then
					if (split_on:find("_Get_", 1, true)) then
						member_help.VarRead = true
						member_help.VarWrite = false
					elseif (split_on:find("_Set_", 1, true)) then
						member_help.VarRead = false
						member_help.VarWrite = true
					end
				end

				local member_definition_parts = split(member_definition, split_on)
				local return_type_name = member_definition_parts[1]:gsub("void", ""):gsub("const char", "string"):gsub(" %*", ""):gsub("%*", ""):gsub("const ", ""):gsub("bool", "boolean")
				member_help.Usage[1].Returns[1] = { Type = convert_numeric_types(return_type_name) }
				
				local parameters_index = member_definition_parts[2]:find("(", 1, true)
				local member_name = member_definition_parts[2]:sub(1, parameters_index - 1)
				local parameters = split(member_definition_parts[2]:sub(parameters_index + 1, -2), ",")

				for i, parameter in ipairs(parameters) do
					parameter = trim(parameter)
							
					if (#parameter > 0) then
						local parameter_parts = split(parameter, " ")

						if (parameter_parts[#parameter_parts]:gsub("*self", "self") ~= "self") then
							local type_name = (table.concat(parameter_parts, " ", 1, #parameter_parts-1)):gsub("const char", "string"):gsub(" %*", ""):gsub("%*", ""):gsub("const ", ""):gsub("bool", "boolean")

							member_help.Usage[1].Args[#member_help.Usage[1].Args+1] = 
							{
								Type = convert_numeric_types(type_name),
								Name = parameter_parts[#parameter_parts]
							}
						else
							if (not member_help.Class) then
								member_help.Class = parameter_parts[1]
							end
						end
					end
				end

				if (member_help.Class) then
					member_help.Name = member_name:sub(#member_help.Class + 1)
				end

				return member_name, member_help
			end

			local function find_members(fusionsystem_content, property_class_name, member_type, search_for)
				local found_at_position = 0
				local next_search_position = 0

				if (member_type == "Variable") then
					search_for = " "..property_class_name.."_"..search_for.."_"
				end

				local discovered_members = {}

				repeat
					found_at_position, next_search_position = fusionsystem_content.ffi_data:find(search_for, next_search_position + 1, true)
					
					if (found_at_position) then
						local member_definition = get_member_definition(fusionsystem_content, found_at_position)
						
						if (not member_definition:find("[;.\n]")) then
							local member_name, member_info = parse_member_definition(member_definition, member_type, search_for)
							discovered_members[member_name] = member_info
						end
					end
				until (not found_at_position)

				return discovered_members
			end

			local function sort_and_sequence_class_members(class_members)
				local sequenced_class_members = {}
				
				for class_name, class_info in pairs(class_members) do
					local seq = {}
				
					for _, member_info in pairs(class_info) do
						seq[#seq+1] = member_info
					end
				
					table.sort(seq, function(a, b) return a.Name < b.Name end)
				
					sequenced_class_members[class_name] = seq
				end

				return sequenced_class_members
			end

			local function get_members()
				local class_properties = {}
				local class_methods = {}
				
				for _, fusionsystem in ipairs(fusion_filenames) do
					local fusionsystem_content = get_fusionsystem_content(fusionsystem[ffi.os])
					local discovered_methods = find_members(fusionsystem_content, nil, "Function", ffi_prefix)
					
					local class_names = {}

					-- First pass for methods
					for name, method_info in pairs(discovered_methods) do
						local class_name = nil
						local method_name = nil
	
						if (method_info.Class) then
							-- Methods that have an identified class
							class_name = method_info.Class
							method_name = method_info.Name
							method_info.Class = nil
						else
							-- Methods without an identified class are usually constructors or other methods that start with an underscore
							local underscore_position = name:find("_", 1, true)
							
							if (underscore_position) then
								class_name = name:sub(1, underscore_position - 1)
								method_name = name:sub(underscore_position)
								method_info.Name = method_name
							end
						end
	
						if (class_name) then
							-- Store the class name even if we don't find any methods, this way we can search for properties later
							if (not class_names[class_name]) then
								class_names[class_name] = {}
							end
								
							if (method_name ~= "_cast" and method_name ~= "_uncast" and method_name ~= "__gc") then
								if (not class_methods[class_name]) then
									class_methods[class_name] = {}
								end
						
								if (method_name == "__new") then
									method_info.ShortHelp = class_name.." constructor"
									method_info.IsConstructor = true
								end
	
								class_methods[class_name][method_name] = method_info
							end
	
							discovered_methods[name] = nil
						end
					end
					
					-- Second pass for methods - match remaining discovered_methods with global functions
					for name, member in pairs(_G) do
						if (type(member) == "function") then
							local class_name = string.match(name, "_(.-)_")
					
							if (class_name) then
								if (not class_names[class_name]) then
									class_names[class_name] = {}
								end

								local method_name = name:gsub("_"..class_name.."_", "")
					
								if (method_name:sub(1, 1) ~= "_") then
									local method_info = discovered_methods[class_name..method_name]
					
									if (method_info) then
										if (not class_methods[class_name]) then
											class_methods[class_name] = {}
										end
					
										method_info.Name = method_name
										class_methods[class_name][method_name] = method_info
										discovered_methods[class_name..method_name] = nil
									end
								end
							end
						end
					end

					-- Properties
					for class_name, _ in pairs(class_names) do
						local getters = find_members(fusionsystem_content, class_name, "Variable", "Get")
						local setters = find_members(fusionsystem_content, class_name, "Variable", "Set")
				
						local properties = {}
				
						-- Add all getters, include matching setters if available
						for property_name, property_info in pairs(getters) do
							if (setters[property_name]) then
								property_info.VarWrite = true
								setters[property_name] = nil
							end
				
							property_info.Name = property_name
							properties[property_name] = property_info
						end
				
						-- Add remaining setters
						for property_name, property_info in pairs(setters) do
							property_info.Name = property_name
							properties[property_name] = property_info
						end
				
						for property_name, property_info in pairs(properties) do
							if (not class_properties[class_name]) then
								class_properties[class_name] = {}
							end
							
							property_info.Class = nil
							class_properties[class_name][property_name] = property_info
						end
					end
				end

				return { Methods = sort_and_sequence_class_members(class_methods), Properties = sort_and_sequence_class_members(class_properties) }
			end

			local members = get_members()
		]===]..
		"bmd.writefile(\""..filename:gsub("\\", "\\\\").."\", { Script = \""..script_name.."\", AppVersion = app:GetVersion(), EnumMap = EnumMap, TagMap = TagMap, Methods = members.Methods, Properties = members.Properties })")

		local wait_start = os.time()
		local timeout = 15 -- seconds

		-- Wait until the file has been written
		while (not bmd.fileexists(filename)) do
			if (os.time() - wait_start >= timeout) then
				error(string.format("Timeout waiting for data file: \"%s\"", filename))
			end

			sleep(200) -- milliseconds
		end

		return bmd.readfile(filename)
	end

	if (force_update_file) then
		data = update_file(data_filename)
	else
		if (bmd.fileexists(data_filename)) then
			data = bmd.readfile(data_filename)

			-- Is the data file created with the same version we're running now?
			if (not (
					data.AppVersion and
					data.AppVersion[1] == version[1] and
					data.AppVersion[2] == version[2] and
					data.AppVersion[3] == version[3] and
					data.AppVersion[4] == version[4] and
					data.Script == script_name and
					data.Properties and
					data.Methods
				)) then
				data = update_file(data_filename)
			end
		else
			-- File wasn't found, create a new one
			data = update_file(data_filename)
		end
	end

	log(string.format("Loaded data file: \"%s\"", data_filename), "verbose")

	return data
end

-- Updates the documented classes with info from the TagMap and discovered methods/properties
local function update_classes(classes, class_methods, class_properties, tag_map)
	local function get_tag_map_parent_path(class_name, path)
		if (not path) then
			path = ""
		end

		for name, value in pairs(tag_map[class_name]) do
			if (value.__parent) then
				local parent_class_name = value.__parent:sub(1, value.__parent:find(".", 1, true) - 1)
				return get_tag_map_parent_path(parent_class_name, "/"..parent_class_name..path)
			end
		end

		return path
	end

	local function add_missing_classes(tbl, is_tag_map)
		if (tbl) then
			for class_name, _ in pairs(tbl) do
				local class_info = classes[class_name]

				if (not class_info) then
					local path = "/"..class_name
					local parent = nil

					if (is_tag_map) then
						path = get_tag_map_parent_path(class_name).."/"..class_name
						local path_parts = split(path, "/")
						local root_class = classes[path_parts[2]]
					
						-- Reassign to the true root class if it exists
						if (root_class and count(root_class.path, "/") >= 2) then
							path = root_class.path.."/"..table.concat( { select(3, table.unpack(path_parts)) } , "/")
						end

						parent = path_parts[#path_parts-1]

						if (#parent == 0) then
							parent = nil
						end
					end
				
					classes[#classes+1] =
					{
						path = path,
						has_members = true,
						name = class_name,
						parent = parent,
					}

					classes[class_name] = classes[#classes]
				else
					if (class_info.has_members == false) then
						class_info.has_members = true
					end
				end
			end
		end
	end

	add_missing_classes(tag_map, true)
	add_missing_classes(class_methods)
	add_missing_classes(class_properties)
end

-- Adds classes to the flat class tree
local function populate_flat_tree(tree, classes)
	local items = {}
	tree:Clear()
	tree.ColumnCount = 1

	for _, class in ipairs(classes) do
		local item = tree:NewItem()
		item.Text[0] = class.name
		items[#items+1] = item
	end

	tree:AddTopLevelItems(items)
	tree:SortByColumn(0, "AscendingOrder")
end

-- To speed up the creation of the nested tree later, we find all the children of each class
local function get_children(classes)
	for _, parent_class in ipairs(classes) do
		local path_parts = split(parent_class.path, "/")
		local sub_classes = {}

		for _, class in ipairs(classes) do
			if (class.path:sub(1, #parent_class.path + 1) == parent_class.path.."/" and count(class.path, "/") == #path_parts) then
				sub_classes[#sub_classes+1] = class
			end
		end

		parent_class.children = sub_classes
	end
end

-- Adds classes to the nested class tree
local function populate_nested_tree(tree, classes)
	local stack = {}
	
	-- Add root classes to the stack
	for _, class in ipairs(classes) do
		-- Root classes are inconsistent,
		-- the ones that are nil seem out of place
		if (class.parent == nil or class.parent == "") then 
			stack[#stack+1] = class
		end
	end
	
	tree:Clear()
	tree.ColumnCount = 1
	local items = {}

	-- Create a new item from each class on the stack
	while #stack > 0 do
		local class = table.remove(stack)

		local item = tree:NewItem()
		item.Text[0] = class.name
		
		if (class.parent_item) then
			class.parent_item:AddChild(item)
			class.parent_item.Expanded = true
			class.parent_item = nil
		else
			items[#items+1] = item
		end

		-- Add children to the stack
		for _, sub_class in ipairs(class.children) do
			sub_class.parent_item = item
			table.insert(stack, sub_class)
		end
	end
	
	tree:AddTopLevelItems(items)
	tree:SortByColumn(0, "AscendingOrder")
end

-- Gets all items (useful for getting all items in a nested tree without traversing the tree)
local function get_all_items(tree)
	return tree:FindItems("*",
	{
		MatchExactly = false,
		MatchFixedString = false,
		MatchContains = false,
		MatchStartsWith = false,
		MatchEndsWith = false,
		MatchCaseSensitive = false,
		MatchRegExp = false,
		MatchWildcard = true,
		MatchWrap = false,
		MatchRecursive = true,
	}, 0)
end

-- Finds tree items based on the given text, wildcards * and ? are supported
local function find_items(tree, text, column)
	return tree:FindItems(text,
	{
		MatchExactly = false,
		MatchFixedString = false,
		MatchContains = true,
		MatchStartsWith = false,
		MatchEndsWith = false,
		MatchCaseSensitive = false,
		MatchRegExp = false,
		MatchWildcard = text:find("[*?]") ~= nil,
		MatchWrap = false,
		MatchRecursive = true,
	}, iif(column == nil, 0, column))
end

-- Selects an item in the given tree by class name
local function select_item(tree, class_name)
	local found_items = tree:FindItems(class_name, 
	{
		MatchExactly = true,
		MatchFixedString = false,
		MatchContains = false,
		MatchStartsWith = false,
		MatchEndsWith = false,
		MatchCaseSensitive = false,
		MatchRegExp = false,
		MatchWildcard = false,
		MatchWrap = false,
		MatchRecursive = true,
	}, 0)

	if (found_items and #found_items > 0) then
		if (found_items[1].Hidden) then
			return nil, string.format("Item \"%s\" is hidden", class_name)
		else
			found_items[1].Selected = true
			tree:ScrollToItem(found_items[1])

			log("Selected: "..class_name, "verbose")

			return true
		end
	else
		return nil, string.format("Item \"%s\" was not found", class_name)
	end
end

-- Deselects any selected items
local function deselect_items(tree)
	local selected_items = tree:SelectedItems()
	
	if (#selected_items > 0) then
		for _, selected_item in ipairs(selected_items)do
			selected_item.Selected = false

			log("Deselected: "..tostring(selected_item.Text[0]), "verbose")
		end
	end

	return #selected_items
end

-- Gets the first item that hasn't been hidden
local function get_first_visible_item(tree)
	for i = 0, tree:TopLevelItemCount() - 1 do
		local item = tree:TopLevelItem(i)
	
		if (not item.Hidden) then
			return item
		end
	end

	return nil
end

-- Hides/unhides items
local function set_item_visibility(tree, classes, hide)
	tree.UpdatesEnabled = false
	
	deselect_items(tree)

	local firstVisibleItem = nil
	
	for i = 0, tree:TopLevelItemCount() - 1 do
		local item = tree:TopLevelItem(i)
	
		if (not (classes[item.Text[0]].has_members) and hide) then
			if (not item.Hidden) then
				item.Hidden = true
			end
		else
			if (item.Hidden) then
				item.Hidden = false
			end
			
			if (not firstVisibleItem) then
				firstVisibleItem = item
			end
		end
	end
	
	if (firstVisibleItem) then
		firstVisibleItem.Selected = true
		tree:ScrollToItem(firstVisibleItem)
	end
	
	tree.UpdatesEnabled = true
	is_filtered = false
end

-- Writes the given text to a file, overwriting any existing file
local function write_string(filename, text)
	if (bmd.fileexists(filename)) then
		assert(os.remove(filename))
	end

	local file_handle = io.open(filename, "a")
	io.output(file_handle)
	io.write(text)
	io.close(file_handle)
end

-- Creates HTML and adds it to the TextEdit widgets
local function display_class(class_name)
	local function get_method_name_html(name, arguments)
		if (arguments == nil) then
			arguments = ""
		end

		-- This will only color the parentheses since arguments have their own style
		return name.."<span style='color: #D0D0D0;'>("..arguments..")</span>"
	end

	local function get_method_name_html_clean(name, arguments)
		if (arguments == nil) then
			arguments = ""
		end

		-- This will only color the parentheses since arguments have their own style
		return name.."("..arguments..")"
	end

	-- TODO: Remove, use get_return_types_html instead
	local function get_return_types(usage)
		local return_types = {}

		if (not usage.Returns) then 
			-- For compatibility with Fusion 9
			return_types[#return_types+1] = usage.Return.Type
		elseif (#usage.Returns > 0) then
			for _, rtn in ipairs(usage.Returns) do
				return_types[#return_types+1] = rtn.Type
			end
		end

		return return_types
	end

	local function get_return_types_html(usage)
		local return_types = {}
		
		if (not usage.Returns) then -- For compatibility with Fusion 9
			if (usage.Return and usage.Return.Type) then
				return_types[#return_types+1] = { Type = iif(usage.Return.Type, usage.Return.Type, ""), Name = iif(usage.Return.Name, usage.Return.Name, "") }
			end
		elseif (#usage.Returns > 0) then
			for _, rtn in ipairs(usage.Returns) do
				return_types[#return_types+1] = { Type = iif(rtn.Type, rtn.Type, ""), Name = iif(rtn.Name, rtn.Name, "") }
			end
		end

		local return_types_html = {}

		for _, return_info in ipairs(return_types) do
			return_types_html[#return_types_html+1] = "<span title='"..return_info.Name.."'>"..return_info.Type.."</span>"
		end

		return "<span class='method_return_type'>"..table.concat(return_types_html, ", ").."</span>"
	end

	local function get_return_types_html_clean(usage)
		local return_types = {}
		
		if (not usage.Returns) then -- For compatibility with Fusion 9
			if (usage.Return and usage.Return.Type) then
				return_types[#return_types+1] = { Type = iif(usage.Return.Type, usage.Return.Type, ""), Name = iif(usage.Return.Name, usage.Return.Name, "") }
			end
		elseif (#usage.Returns > 0) then
			for _, rtn in ipairs(usage.Returns) do
				return_types[#return_types+1] = { Type = iif(rtn.Type, rtn.Type, ""), Name = iif(rtn.Name, rtn.Name, "") }
			end
		end

		local return_types_html = {}

		for _, return_info in ipairs(return_types) do
			return_types_html[#return_types_html+1] = return_info.Type
		end

		return table.concat(return_types_html, ", ")
	end

	local function get_class_code_name(class_name)
		class_name = class_name:gsub("%.", "_")

		if (class_name:find("%s")) then
			-- Remove spaces and capitalize the first character in each word.
			-- This takes care of edge cases such as the "Timeline item" and "Media pool item" classes.
			local new_name = {}

			for _, name in pairs(split(class_name, " ")) do
				new_name[#new_name+1] = name:sub(1, 1):upper()..name:sub(2, #name)
			end

			return table.concat(new_name, "")
		else
			return class_name
		end
	end

	local function get_usage_html(class_name, function_help)
		local rows = {}

		for i, usage in ipairs(function_help.Usage) do
			local arguments = {}

			if (#usage.Args > 0) then
				for _, argument in ipairs(usage.Args) do
					arguments[#arguments+1] =
						iif(argument.Optional, "<span class='arg_optional'>[", "")..
						"<span class='arg_type'>"..argument.Type.."</span> "..
						"<span class='arg_name'>"..argument.Name.."</span>"..
						iif(argument.Optional, "]</span>", "")
				end
			end
			
			rows[i] = 
				"<div class='description method_usage'>"..
					get_return_types_html(usage).." "..
					get_class_code_name(class_name)..iif(function_help.IsConstructor, "", ":")..
					"<span class='method'>"..get_method_name_html(iif(function_help.IsConstructor, "", function_help.Name), table.concat(arguments, ", ")).."</span>"..
				"</div>\n"
		end

		return table.concat(rows)
	end

	local function get_usage_html_clean(class_name, function_help)
		local rows = {}

		for i, usage in ipairs(function_help.Usage) do
			local arguments = {}

			if (#usage.Args > 0) then
				for _, argument in ipairs(usage.Args) do
					arguments[#arguments+1] =
						iif(argument.Optional, "[", "")..
						argument.Type.." "..
						argument.Name..
						iif(argument.Optional, "]", "")
				end
			end

			rows[i] = get_return_types_html_clean(usage).." "..
					get_class_code_name(class_name)..
					iif(function_help.IsConstructor, "", ":")..
					get_method_name_html_clean(iif(function_help.IsConstructor, "", function_help.Name), table.concat(arguments, ", "))
		end

		return rows
	end
	
	local function get_see_also_html(class_name, member_help)
		local see_also_members = {}

		if (member_help.SeeAlso) then
			for _, see_also in ipairs(member_help.SeeAlso) do
				if (#see_also.Text > 0) then
					local fixed_see_also_text = see_also.Text	
					
					-- Fix incorrect references
					if (class_name == "PlainInput" and member_help.Name == "GetKeyFrames" and fixed_see_also_text == "Tool:GetKeyFrames") then
						fixed_see_also_text = "Operator:GetKeyFrames"	
					elseif (class_name == "Operator" and member_help.Name == "GetKeyFrames" and fixed_see_also_text == "Input:GetKeyFrames") then
						fixed_see_also_text = "PlainInput:GetKeyFrames"	
					elseif (class_name == "Operator" and member_help.Name == "ConnectInput" and fixed_see_also_text == "Tool") then
						fixed_see_also_text = ""
					elseif (class_name == "FuFrame" and member_help.Name == "GetViewList" and fixed_see_also_text == "SwitchControlView") then
						fixed_see_also_text = "ChildFrame:SwitchControlView"
					elseif (class_name == "FuFrame" and member_help.Name == "GetViewList" and fixed_see_also_text == "GetMainViewList") then
						fixed_see_also_text = "ChildFrame:GetMainViewList"
					elseif (class_name == "GLView" and member_help.Name == "GetPrefs" and fixed_see_also_text == "ShowPrefs") then
						fixed_see_also_text = "Fusion:ShowPrefs"
					elseif (class_name == "GLView" and member_help.Name == "GetPrefs" and fixed_see_also_text == "SetPrefs") then
						fixed_see_also_text = "Fusion:SetPrefs"
					end

					if (#fixed_see_also_text > 0) then
						if (fixed_see_also_text:find(":")) then
							-- Reference to a method in another class
							local method_reference = split(fixed_see_also_text, ":")

							see_also_members[#see_also_members+1] = "<a href='displayclass://"..method_reference[1].."#"..method_reference[2].."' class='method'>"..get_method_name_html(fixed_see_also_text).."</a>"
						elseif (fixed_see_also_text:find("%.")) then
							-- Reference to a property in another class
							local property_reference = split(fixed_see_also_text, ".")
							see_also_members[#see_also_members+1] = "<a href='displayclass://"..property_reference[1].."#"..property_reference[2].."' class='property'>"..fixed_see_also_text.."</a>"
						else
							if (app:GetHelpRaw(fixed_see_also_text)) then
								-- Reference to the root of another class
								see_also_members[#see_also_members+1] = "<a href='displayclass://"..fixed_see_also_text.."' class='description'>"..fixed_see_also_text.."</a>"
							else
								local target_member_help = app:GetHelpRaw(class_name, fixed_see_also_text)

								if (target_member_help) then
									if (target_member_help.Type == "Function") then
										-- Reference to a method in the same class
										see_also_members[#see_also_members+1] = "<a href='#"..fixed_see_also_text.."' class='method'>"..get_method_name_html(fixed_see_also_text).."</a>"
									elseif (target_member_help.Type == "Variable") then
										-- Reference to a property in the same class
										see_also_members[#see_also_members+1] =	"<a href='#"..fixed_see_also_text.."' class='property'>"..fixed_see_also_text.."</a>"
									else
										-- Reference to an unknown member type in the same class
										see_also_members[#see_also_members+1] = fixed_see_also_text
									end
								else
									-- Reference not found
									see_also_members[#see_also_members+1] = fixed_see_also_text

									-- Some examples:
									-- SplineEditorView:GetClipBoard() -> SetClipBoard()
									-- TimelineView:GetClipBoard() -> SetClipBoard()
								end
							end
						end
					end
				end
			end

			return iif(#see_also_members > 0, "<div class='see_also'>See also: "..table.concat(see_also_members, ", ").."</div>", "")
		else
			-- SeeAlso is not supported in Fusion 9
			return ""
		end
	end

	local function get_see_also_html_clean(class_name, member_help)
		local see_also_members = {}

		if (member_help.SeeAlso) then
			for _, see_also in ipairs(member_help.SeeAlso) do
				if (#see_also.Text > 0) then
					local fixed_see_also_text = see_also.Text	
					
					-- Fix incorrect references
					if (class_name == "PlainInput" and member_help.Name == "GetKeyFrames" and fixed_see_also_text == "Tool:GetKeyFrames") then
						fixed_see_also_text = "Operator:GetKeyFrames"	
					elseif (class_name == "Operator" and member_help.Name == "GetKeyFrames" and fixed_see_also_text == "Input:GetKeyFrames") then
						fixed_see_also_text = "PlainInput:GetKeyFrames"	
					elseif (class_name == "Operator" and member_help.Name == "ConnectInput" and fixed_see_also_text == "Tool") then
						fixed_see_also_text = ""
					elseif (class_name == "FuFrame" and member_help.Name == "GetViewList" and fixed_see_also_text == "SwitchControlView") then
						fixed_see_also_text = "ChildFrame:SwitchControlView"
					elseif (class_name == "FuFrame" and member_help.Name == "GetViewList" and fixed_see_also_text == "GetMainViewList") then
						fixed_see_also_text = "ChildFrame:GetMainViewList"
					elseif (class_name == "GLView" and member_help.Name == "GetPrefs" and fixed_see_also_text == "ShowPrefs") then
						fixed_see_also_text = "Fusion:ShowPrefs"
					elseif (class_name == "GLView" and member_help.Name == "GetPrefs" and fixed_see_also_text == "SetPrefs") then
						fixed_see_also_text = "Fusion:SetPrefs"
					end

					if (#fixed_see_also_text > 0) then
						if (fixed_see_also_text:find(":")) then
							-- Reference to a method in another class
							local method_reference = split(fixed_see_also_text, ":")
							local nextID = #see_also_members+1
							see_also_members[nextID] = {}
							see_also_members[nextID]["method"] = method_reference[1]
							see_also_members[nextID]["name"] = method_reference[2]
						elseif (fixed_see_also_text:find("%.")) then
							-- Reference to a property in another class
							local property_reference = split(fixed_see_also_text, ".")
							local nextID = #see_also_members+1
							see_also_members[nextID] = {}
							see_also_members[nextID]["property"] = property_reference[1]
							see_also_members[nextID]["name"] = property_reference[2]
						else
							if (app:GetHelpRaw(fixed_see_also_text)) then
								-- Reference to the root of another class
								local nextID = #see_also_members+1
								see_also_members[nextID] = {}
								see_also_members[nextID]["name"] = fixed_see_also_text
							else
								local target_member_help = app:GetHelpRaw(class_name, fixed_see_also_text)

								if (target_member_help) then
									if (target_member_help.Type == "Function") then
										-- Reference to a method in the same class
										local nextID = #see_also_members+1
										see_also_members[nextID] = {}
										see_also_members[nextID]["name"] = fixed_see_also_text
									elseif (target_member_help.Type == "Variable") then
										-- Reference to a property in the same class
										local nextID = #see_also_members+1
										see_also_members[nextID] = {}
										see_also_members[nextID]["name"] = fixed_see_also_text
									else
										-- Reference to an unknown member type in the same class
										local nextID = #see_also_members+1
										see_also_members[nextID] = {}
										see_also_members[nextID]["name"] = fixed_see_also_text
									end
								else
									-- Reference not found
									local nextID = #see_also_members+1
									see_also_members[nextID] = {}
									see_also_members[nextID]["name"] = fixed_see_also_text

									-- Some examples:
									-- SplineEditorView:GetClipBoard() -> SetClipBoard()
									-- TimelineView:GetClipBoard() -> SetClipBoard()
								end
							end
						end
					end
				end
			end

			return see_also_members
		else
			-- SeeAlso is not supported in Fusion 9
			return {}
		end
	end

	local function get_description_html(member_help)
		local descriptions = {}

		for _, description in ipairs(member_help.Description) do
			if (#description.Text > 0) then
				descriptions[#descriptions+1] = "<pre class='text description'>"..trim(description.Text).."</pre>\n"
			end
		end

		return table.concat(descriptions)
	end

	local function get_description_html_clean(member_help)
		local descriptions = {}

		for _, description in ipairs(member_help.Description) do
			if (#description.Text > 0) then
				descriptions[#descriptions+1] = trim(description.Text)
			end
		end

		return table.concat(descriptions)
	end

	local function parse_attribute(attribute_name)
		local attribute_parts = split(attribute_name:sub(4), "_")
		local attribute_type = attribute_parts[1]
		local attribute_name_only = attribute_parts[2]

		if (attribute_type == "S") then
			attribute_type = "string"
		elseif (attribute_type == "B") then
			attribute_type = "boolean"
		elseif (attribute_type == "N") then
			attribute_type = "number (float)"
		elseif (attribute_type == "I") then
			attribute_type = "number (integer)"
		elseif (attribute_type == "H") then
			attribute_type = "handle" --TODO: Pointer?
		elseif (attribute_type == "NT") then
			attribute_type = "table { number (float) }"
		elseif (attribute_type == "IT") then
			attribute_type = "table { number (integer) }"
		elseif (attribute_type == "ST") then
			attribute_type = "table { string }"
		elseif (attribute_type == "BT") then
			attribute_type = "table { bool }"
		else
			attribute_type = "[unknown] (\""..attribute_type.."\")"
		end

		return attribute_type, attribute_name_only
	end

	local function get_attribute_value_html(value)
		if (type(value) == "table") then
			local output_html = dumptostring(value)
			output_html = output_html:gsub("\\n", "\n") -- Fix for Fusion 9 bug in dumptostring()

			-- Remove the first line which is just a table header created by dumptostring()
			-- then replace line breaks with <br /> tags
			return output_html:sub(output_html:find("\n") + 1, 1, true):gsub("\n", "<br />")
		else
			return tostring(value)
		end
	end

	local function get_attribute_value_html_clean(value)
		if (type(value) == "table") then
			local output_html = dumptostring(value)
			output_html = output_html:gsub("\\n", "\n") -- Fix for Fusion 9 bug in dumptostring()

			return tostring(output_html:sub(output_html:find("\n") + 1, 1, true))
		else
			return tostring(value)
		end
	end

	local function display_properties(header, info_text, output, class_name, variables_help)
		if (variables_help and #variables_help > 0) then
			table.insert(output, "<h2>"..header.."</h2>")
			local listID = #propertiesList+1
			propertiesList[listID] = {}
			propertiesList[listID]["header"] = header

			
			if (info_text and #info_text > 0) then
				table.insert(output, "<div class='text info'>"..info_text.."</div>")
				propertiesList[listID]["info_text"] = info_text
			end
			
			table.insert(output, "<table cellspacing='7'>\n")

			propertiesList[listID]["items"] = {}
			for i, variable_help in ipairs(variables_help) do
				table.insert(output, "<tr><td colspan='2' id='"..variable_help.Name.."'><hr /></td></tr>\n")

				local return_types = {}
				local types_text = ""

				for _, usage in ipairs(variable_help.Usage) do
					for _, return_type in ipairs(get_return_types(usage)) do
						return_types[#return_types+1] = return_type
					end
				end

				if (#return_types > 0) then
					types_text = string.format("Type%s: %s", iif(#return_types == 1, "", "s"), table.concat(return_types, ", "))
				end

				local access = { text = "", class = "" }

				if (variable_help.VarRead == nil and variable_help.VarWrite == nil) then
					-- No info, don't show anything
				elseif (variable_help.VarRead and variable_help.VarWrite) then
					access = { text = "Read/write", class = "read_write" }
				elseif (variable_help.VarRead and variable_help.VarWrite == false) then
					access = { text = "Read-only", class = "read_only" }
				elseif (variable_help.VarRead == false and variable_help.VarWrite) then
					access = { text = "Write-only", class = "write_only" }
				else
					-- Shouldn't happen
				end

				table.insert(output, "<tr>\n")
				table.insert(output,
					"<td width='"..cell_width.."' class='text'>"..
						"<div class='property'>"..variable_help.Name.."</div>"..
						"<div class='property_return_type'>"..types_text.."</div>"..
						"<div class='access "..access.class.."'>"..access.text.."</div>"..
					"</td>\n")
				propertiesList[listID]["items"][i] = {}
				propertiesList[listID]["items"][i]["name"] = variable_help.Name
				propertiesList[listID]["items"][i]["return_type"] = types_text
				propertiesList[listID]["items"][i]["access_class"] = access.class
				table.insert(output,
					"<td width='100%' class='text help'>"..
						"<p class='help'>"..variable_help.ShortHelp.."</p>"..
						get_description_html(variable_help)..
						get_see_also_html(class_name, variable_help)..
					"</td>\n")
				table.insert(output, "</tr>\n")
				propertiesList[listID]["items"][i]["short_help"] = variable_help.ShortHelp
				propertiesList[listID]["items"][i]["description"] = get_description_html_clean(variable_help)
				propertiesList[listID]["items"][i]["see_also"] = get_see_also_html_clean(class_name, variable_help)
			end

			table.insert(output, "<tr><td colspan='2'><hr /></td></tr>\n")
			table.insert(output, "</table>\n")
		end
	end

	local function display_methods(header, info_text, output, class_name, functions_help)
		if (functions_help and #functions_help > 0) then
			local listID = #methodList+1
			table.insert(output, "<h2>"..header.."</h2>")
			methodList[listID] = {}
			methodList[listID]["header"] = header
			
			if (info_text and #info_text > 0) then
				table.insert(output, "<div class='text info'>"..info_text.."</div>")
			end
			methodList[listID]["info_text"] = info_text
			
			table.insert(output, "<table cellspacing='7'>\n")

			methodList[listID]["items"] = {}
			for i, function_help in ipairs(functions_help) do
				table.insert(output, "<tr><td colspan='2' id='"..function_help.Name.."'><hr /></td></tr>\n")
				table.insert(output, "<tr>\n")
				table.insert(output,
					"<td width='"..cell_width.."' class='text'>"..
						"<div class='method'>"..get_method_name_html(iif(function_help.IsConstructor, class_name, function_help.Name)).."</div>"..
					"</td>\n")
				table.insert(output,
					"<td width='100%' class='text help'>"..
						"<p class='help'>"..function_help.ShortHelp.."</p>"..
						get_usage_html(class_name, function_help)..
						get_description_html(function_help)..
						get_see_also_html(class_name, function_help)..
					"</td>\n")
				table.insert(output, "</tr>\n")
				methodList[listID]["items"][i] = {}
				methodList[listID]["items"][i]["name"] = iif(function_help.IsConstructor, class_name, function_help.Name)
				methodList[listID]["items"][i]["short_help"] = function_help.ShortHelp
				methodList[listID]["items"][i]["usage"] = get_usage_html_clean(class_name, function_help)
				methodList[listID]["items"][i]["description"] = get_description_html_clean(function_help)
				methodList[listID]["items"][i]["see_also"] = get_see_also_html_clean(class_name, function_help)
			end

			table.insert(output, "<tr><td colspan='2'><hr /></td></tr>\n")
			table.insert(output, "</table>\n")
		end
	end

	local function display_tags(output, class_name)
		local function get_tag_type(type_name, enum_name)
			if (type_name == nil) then
				return nil
			elseif (type_name == "Bool") then
				return "boolean"
			elseif (type_name == "Enum") then
				if (enum_name) then
					return enum_name
				else
					return "enum"
				end
			elseif (type_name == "UInt") then
				return "number (unsigned integer)"
			else
				log("Unknown type: "..type_name)
				return nil
			end
		end

		local function get_enum(enum_fullpath)
			if (enum_fullpath) then
				local enum_value_parts = split(enum_fullpath, ".")
				
				return
				{
					FullPath = enum_fullpath,
					Name = enum_value_parts[2],
					Values = enum_map[enum_value_parts[1]][enum_value_parts[2]]
				}
			else
				return nil
			end
		end

		local function get_method_tags(version, tbl)
			-- v17+ separated the table into __values, __keys and __order
			if (version[1] < 17) then
				return tbl
			else
				return tbl.__values
			end
		end

		local function get_method_tags_by_value(version, tbl, value)
			-- v17+ separated the table into __values, __keys and __order
			if (version[1] < 17) then
				return tbl[value]
			else
				return tbl.__keys[value]
			end
		end

		local tags = tag_map[class_name]
		
		if (tags) then
			
			table.insert(output, "<h2>Tag Map</h2>")
			table.insert(output, "<table cellspacing='7'>\n")
			table.insert(output, "<tr><td colspan='3'><hr /></td></tr>\n")

			local i_method = 1
			for method, method_tags in pairs(tags) do
				tagsList[i_method] = {}
				local parent_tag = nil
				local parent_tag_html = ""

				for key, value in pairs(method_tags) do
					if (key == "__parent") then
						parent_tag = value
						break
					end
				end
				
				if (parent_tag) then
					parent_tag_html = "<div class='tag_return_type'> : "..parent_tag.."</div>"
				end

				table.insert(output,
					"<tr>\n"..
						"<td width='"..cell_width.."' class='text'>"..
							"<div class='tag_method'>"..method.."</div>"..
							parent_tag_html..
						"</td>\n"..
						"<td width='"..cell_width.."'></td>"..
						"<td width='100%'></td>"..
					"</tr>\n")
				table.insert(output, "<tr><td colspan='3'><hr /></td></tr>\n")
				tagsList[i_method]["method"] = method
				tagsList[i_method]["parent_tag"] = parent_tag
				
				local i_tags = 1
				tagsList[i_method]["tags"] = {}
				for key, value in pairs(get_method_tags(runtime_version, method_tags)) do
					tagsList[i_method]["tags"][i_tags] = {}
					if (type(key) == "number") then
						local tag_table = get_method_tags_by_value(runtime_version, method_tags, value)
						local key_type = get_tag_type(tag_table.Type, tag_table.Enum)
						local key_set = tag_table.Set

						table.insert(output,
							"<tr>\n"..
								"<td></td>"..
								"<td class='text'>\n"..
									"<div class='help tag'>"..value.."</div>\n")
						tagsList[i_method]["tags"][i_tags]["value"] = value

						if (key_type) then
							table.insert(output, "<div class='tag_return_type'>Type: "..key_type.."</div></td>\n")
							tagsList[i_method]["tags"][i_tags]["key_type"] = key_type

							local enum = get_enum(tag_table.Enum)
							if (enum) then
								table.insert(output, "<td><dl><dt class='text help'>Possible "..enum.Name.." values:<br /></dt>\n")
								tagsList[i_method]["tags"][i_tags]["enum_name"] = enum.Name
								local i_enum = 1
								tagsList[i_method]["tags"][i_tags]["enum_value"] = {}
								for enum_index, enum_value in pairs(enum.Values) do
									if (type(enum_index) == "number") then
										table.insert(output, "<dd class='text description'>\t"..enum_value.."</dd>\n")
										tagsList[i_method]["tags"][i_tags]["enum_value"][i_enum] = enum_value
										i_enum = i_enum + 1
									end
								end

								table.insert(output, "</dl></td>\n")
							else
								table.insert(output, "<td></td>\n")
							end
						else
							table.insert(output, "</td>\n")
						end

						table.insert(output, "</tr>\n")
						table.insert(output, "<tr><td colspan='3'><hr /></td></tr>\n")
						i_tags = i_tags + 1
					end
				end
				i_method = i_method + 1
			end
			table.insert(output, "</table>\n")
		end
	end

	local function display_registry(output, class_name)
		local reg_attributes = registry_index[class_name]

		if (reg_attributes) then
			table.insert(output, "<h2>Registry Attributes</h2>")
			table.insert(output, "<table cellspacing='7'>\n")
			table.insert(output, "<tr><td colspan='2'><hr /></td></tr>\n")

			local sorted_attributes = {}

			for key, value in pairs(reg_attributes) do
				if (#tostring(value) > 0 or attribute_type == "string") then -- Ignore attributes like empty integers
					local attribute_type, attribute_name = parse_attribute(key)
					sorted_attributes[#sorted_attributes+1] = { Name = attribute_name, FullName = key, Type = attribute_type, Value = value }
				end
			end

			-- Sort by name without the REG prefix
			table.sort(sorted_attributes, function(a, b) return a.Name < b.Name end)

			for i, attribute in ipairs(sorted_attributes) do
				local class_type_string = ""
				local tooltip = registry_attribute_descriptions[attribute.FullName] or ""

				-- Show the enum value that equals the current ClassType, if it's a known value
				if (attribute.FullName == "REGI_ClassType") then
					local class_type_by_id = class_type_index[attribute.Value]
					
					if (class_type_by_id) then
						class_type_string = " = "..class_type_by_id
					end
				end

				table.insert(output, "<tr>\n")
				table.insert(output,
					"<td width='"..cell_width.."' class='text'>"..
						"<div class='attribute' title='"..tooltip.."'>"..attribute.FullName.."</div>"..
						"<div class='attribute_return_type'>Type: "..attribute.Type.."</div>"..
					"</td>\n")
				table.insert(output,
					"<td width='100%' class='text attribute_value'>"..get_attribute_value_html(attribute.Value)..iif(class_type_string, class_type_string, "").."</td>\n")
				table.insert(output, "</tr>\n")
				table.insert(output, "<tr><td colspan='2'><hr /></td></tr>\n")
				registryList[i] = {}
				registryList[i]["full_name"] = attribute.FullName
				registryList[i]["value"] = attribute.Type
				registryList[i]["type"] = get_attribute_value_html_clean(attribute.Value)..iif(class_type_string, class_type_string, "")
			end

			table.insert(output, "</table>\n")
		end
	end

	local function copy_members(class_name, class_members)
		if (class_members == nil) then
			return nil
		end

		local members_to_copy = class_members[class_name]

		-- We need to use a copy of the table so we can move parameters to the main Methods/Properties if needed, without affecting the original table
		if (members_to_copy) then
			return { table.unpack(members_to_copy) }
		else
			return nil
		end
	end

	local function get_member_index(member_name, discovered_members)
		for i, member_info in ipairs(discovered_members) do
			if (member_info.Name == member_name) then
				return i
			end
		end

		return nil
	end

	local function get_header_html(class)
		local class_inheritance = split(class.path:sub(2), "/")
		local header = {}
		
		table.insert(header, "<body bgcolor='#212126'>\n")
		table.insert(header,
		[[
			<style>
				body { font-family: Segoe UI, SegoeUI, Segoe WP, Helvetica Neue, Helvetica, Tahoma, Arial, sans-serif; }
				h1 { color: #D0D0D0; font-size: 40px; font-weight: 600; }
				h2 { color: #D0D0D0; margin-top: 24px; font-size: 28px; font-weight: 600; }
				h3 { color: #D0D0D0; font-size: 16px; font-weight: 400; }

				.page { margin-left: 10px; margin-right: 10px; }

				.parent { color: #D0D0D0; }
				.parent_disabled { color: #919191; }
			</style>
		]])
		table.insert(header, "<div class='page'>\n")
		table.insert(header, "<table><tr>")
		table.insert(header, "<td width='99%'><h1>"..class.name.."</h1></td>")
		headerList["name"] = class.name
		
	
		local qt_info = qt_documentation[class_name]

		if (qt_info and type(qt_info) == "table") then
			table.insert(header, "<td width='1%'><nobr><p align='right'>Qt: <a href='"..qt_info.Url.."' title='View Qt documentation at\n"..qt_info.Url.."' style='color: #4376A1;'>"..qt_info.Name.."</a></p></nobr></td>\n")
			headerList["qt"] = {}
			headerList["qt"]["name"] = qt_info.Name
			headerList["qt"]["url"] = qt_info.Url
		end

		table.insert(header, "</tr></table>\n")

		if (class.parent and #class.parent > 0) then
			table.insert(header, "<h3 style='margin-left: 14px;'>")
			headerList["class_inheritance"] = {}

			for i = #class_inheritance - 1, 1, -1 do
				if (classes[class_inheritance[i]].has_members or (not (windowItems.CheckBoxHideEmptyClasses.Checked and windowItems.CheckBoxHideEmptyClasses.Visible))) then
					table.insert(header, " :&nbsp;<a href='displayclass://"..class_inheritance[i].."' class='parent'>"..class_inheritance[i].."</a>")	
				else
					table.insert(header, " :&nbsp;<span class='parent_disabled' title='To navigate to this class, uncheck\n\"Hide Classes Without Members\"'>"..class_inheritance[i].."</span>")
				end
				headerList["class_inheritance"][i] = class_inheritance[i]
			end

			table.insert(header, "</h3>\n")
		end

		table.insert(header, "</div>\n")
		table.insert(header, "</body>\n")

		return table.concat(header)
	end

	local function update_existing_members(updated_members, members_help)
		local function replace_help_fields(updated_members, original_help, updated_help, member_index)
			
			local fields 
			
			if (runtime_version[1] == 9) then
				fields = table.pack("Usage", "ShortHelp", "Description")	
			else
				fields = table.pack("Usage", "ShortHelp", "Description", "SeeAlso")	
			end
			
			local remove_updated_member = false

			for _, field in ipairs(fields) do
				local original_field_has_value = #original_help[field] > 0
				local updated_field_has_value = #updated_help[field] > 0

				if (original_field_has_value and field == "Description") then
					original_field_has_value = original_help[field].Text ~= nil and #original_help[field].Text > 0
				end

				if (not original_field_has_value and updated_field_has_value) then
					-- Move field value from the updated member to the existing member
					original_help[field] = updated_help[field]
					remove_updated_member = true
				elseif (original_field_has_value) then
					-- Don't need this updated member since the original field already has a value
					remove_updated_member = true
				else
					-- Don't do anything
				end
			end

			if (remove_updated_member) then
				table.remove(updated_members, member_index)
			end
		end

		if (updated_members) then
			for _, member_help in ipairs(members_help) do
				local method_index = get_member_index(member_help.Name, updated_members)

				if (method_index) then
					local updated_help = updated_members[method_index]
					replace_help_fields(updated_members, member_help, updated_help, method_index)
				end
			end
		end
	end

	local class = classes[class_name]
	local class_help = app:GetHelpRaw(class.name)
	local output = {}

	table.insert(output,
	[[
		<style>
			body { font-family: Segoe UI, SegoeUI, Segoe WP, Helvetica Neue, Helvetica, Tahoma, Arial, sans-serif; }
			h1 { color: #D0D0D0; font-size: 40px; font-weight: 600; }
			h2 { color: #D0D0D0; margin-top: 24px; font-size: 28px; font-weight: 600; }
			h3 { color: #D0D0D0; font-size: 16px; font-weight: 400; }
			td { font-size: 13px; font-weight: 400; vertical-align: text-top; }
			th { font-size: 24px; font-weight: 600; }
			pre { white-space: pre-wrap; }

			.page { margin-left: 10px; margin-right: 10px; }
			.text { font-family: ]]..iif(ffi.os == "Windows", "Consolas, Lucida Console, Courier New", iif(ffi.os == "OSX", "SF Mono, Andale Mono, Courier", "Courier New, Monospace"))..[[; }
			.help { font-weight: 600; color: #8DCEAA; }
			.description { font-weight: 600; color: #448F65; }
			.see_also { margin-top: 24px; color: #448F65; }
			.info { margin-left: 2px; font-size: 12px; color: #D0D0D0; }

			.property { font-weight: 600; color: #D0D0D0; }
			.property_return_type { font-size: 12px; color: #7E7E7E; }
			.access { margin-top: 8px; font-size: 12px; }
			.read_write { color: #4376A1; }
			.read_only { color: #E64B3D; }
			.write_only { color: #EB6E00; }

			.method { font-weight: 600; color: #009899; }
			.method_usage { margin: 12px 0px 12px 0px; }
			.method_return_type { color: #7E7E7E; }
			.arg_type { color: #7E7E7E; }
			.arg_name { color: #D0D0D0; }
			.arg_optional { font-style: italic; }

			.attribute { font-weight: 600; color: #C6A077; }
			.attribute_return_type { font-size: 12px; color: #7E7E7E; }
			.attribute_value { color: #D0D0D0; }

			.tag { font-weight: 600; color: #C6A077; }
			.tag_return_type { font-size: 12px; color: #7E7E7E; }
			.tag_method { color: #D0D0D0; }
		</style>
	]])
	
	table.insert(output, "<body bgcolor='#212126'>\n")
	
	local variables_help = {}
	local functions_help = {}
	local discovered_properties = copy_members(class_name, discovered_class_properties)
	local discovered_methods = copy_members(class_name, discovered_class_methods)
	local added_properties = copy_members(class_name, added_class_members.Properties)
	local added_methods = copy_members(class_name, added_class_members.Methods)
	table.insert(output, "<div class='page'>\n")

	if (class_help) then
		if (#class_help.ShortHelp == 0 and added_class_members.Classes and added_class_members.Classes[class_name] and added_class_members.Classes[class_name].ShortHelp) then
			class_help.ShortHelp = added_class_members.Classes[class_name].ShortHelp
		end

		table.insert(output, "<p class='text help'>"..class_help.ShortHelp.."</p>\n")
		headerList["short_help"] = class_help.ShortHelp
	
		if (#class_help.Members > 0) then
			table.sort(class_help.Members)
		
			for i, member in ipairs(class_help.Members) do
				local member_help = app:GetHelpRaw(class_name, member)

				if(member_help.Type:lower() == "variable") then
					variables_help[#variables_help+1] = member_help
				elseif (member_help.Type:lower() == "function") then
					functions_help[#functions_help+1] = member_help
				else
					error("GetHelpRaw reported unknown type: "..member_help.Type)
				end
			end
		end
	end

	update_existing_members(discovered_properties, variables_help)
	update_existing_members(added_properties, variables_help)
	update_existing_members(discovered_methods, functions_help)
	update_existing_members(added_methods, functions_help)

	display_properties("Properties", "", output, class_name, variables_help)
	display_properties("Discovered Properties", "Discovered properties might be available in many contexts, but most typically in Fuse scripts", output, class_name, discovered_properties)
	display_properties("Added Properties", "Manually added properties are known but not documented or discoverable", output, class_name, added_properties)
	display_methods("Methods", "", output, class_name, functions_help)
	display_methods("Discovered Methods", "Discovered methods might be available in many contexts, but most typically in Fuse scripts", output, class_name, discovered_methods)
	display_methods("Added Methods", "Manually added methods are known but not documented or discoverable", output, class_name, added_methods)
	display_tags(output, class_name)
	display_registry(output, class_name)

	table.insert(output, "</div>\n")
	table.insert(output, "</body>\n")
	local html = table.concat(output)
	

	windowItems.TextEditHeader.UpdatesEnabled = false
	windowItems.TextEditHelp.UpdatesEnabled = false
	windowItems.TextEditHeader.HTML = get_header_html(class)
	windowItems.TextEditHelp.HTML = html
	windowItems.TextEditHeader.UpdatesEnabled = true
	windowItems.TextEditHelp.UpdatesEnabled = true

	last_displayed_class = class_name

	--print("Creating "..class_name:gsub(" ", "_")..".md")
	--createMarkdown(class_name)
	createPythonDocs(class_name)
	-- Clear all lists
	propertiesList = {}
	methodList = {}
	tagsList = {}
	registryList = {}
	headerList = {}

	log("Displayed: "..class_name, "verbose")

	-- Added for convenience, exports the current class to an HTML file
	--TODO: Add GUI
	--local desktop_path = iif(ffi.os == "Windows", os.getenv("USERPROFILE"), os.getenv("HOME")).."/Desktop"
	--write_string(desktop_path.."/class_browser_original.html", html) -- The original HTML
	--write_string(desktop_path.."/class_browser_qt.html", windowItems.TextEditHelp.HTML) -- HTML from Qt control
end

-- Creates the main window
local function create_window()
	local left_pane_size = 380

	local window = dispatcher:AddWindow(
	{
		ID = "ClassBrowser",
		WindowTitle = script_name,
		WindowFlags =
		{
			Window = true,
			WindowStaysOnTopHint = false,
		},

		-- Uncomment to make it a modal window that doesn't let Resolve kidnap the keyboard
		--WindowModality = "WindowModal",

		ui:VGroup
		{
			ui:HGroup
			{
				Weight = 0,
			
				ui:LineEdit
				{
					--Weight = 1,
					ID = "LineEditFilter",
					MinimumSize = { left_pane_size, 0 }, MaximumSize = { left_pane_size, 16777215 },
					PlaceholderText = "Filter class name...",
					Events = { ReturnPressed = true },
				},

				ui:HGap(0, 1),

				ui:Button
				{
					Weight = 0,
					ID = "FolderButton",
					Text = "Open Script Folder",
					ToolTip = "Open the folder that contains the \""..script_file.Filename.."\" script",
				},

				ui:Button
				{
					Weight = 0,
					ID = "AboutButton",
					Text = "About",
					ToolTip = "Go to the forum post associated with this script",
				},
			},

			ui:HGroup
			{
				Weight = 1,

				ui:VGroup
				{
					Weight = 0,

					ui:Tree
					{
						ID = "TreeFlat", 
						Weight = 1,
						HeaderHidden = true,
						MinimumSize = { left_pane_size, 100 },
						Events = { ItemSelectionChanged = true },
					},

					ui:Tree
					{
						ID = "TreeNested", 
						Weight = 1,
						HeaderHidden = true,
						MinimumSize = { left_pane_size, 100 },
						Events = { ItemSelectionChanged = true },
						Hidden = true,
					},
				},
	
				ui:VGroup
				{
					Weight = 1,

					ui:TextEdit
					{
						Weight = 1, -- Added for compatibility with v16
						ID = "TextEditHeader",
						ReadOnly = true,
						MinimumSize = { 420, 90 },
						MaximumSize = { 16777215, 90 }, -- Added for compatibility with v16
						Events = { AnchorClicked = true },
						StyleSheet = "QTextEdit { border: 1px solid black; }",
						WordWrapMode = "NoWrap",
					},

					ui:TextEdit
					{
						Weight = 1,
						ID = "TextEditHelp",
						ReadOnly = true,
						MinimumSize = { 420, 100 },
						Events = { AnchorClicked = true },
						StyleSheet = "QTextEdit { border: 1px solid black; }",
					},
				},
			},

			ui:VGap(1),

			ui:HGroup
			{
				Weight = 0,

				ui:Button
				{
					Weight = 0,
					ID = "ButtonGenerate",
					Text = "Generate .md",
					MinimumSize = { 100, 1 },
				},

				ui:Button
				{
					Weight = 0,
					ID = "ButtonFlat",
					Text = "Flat View",
					Checkable = true,
					AutoExclusive = true,
					MinimumSize = { 100, 1 },
					Events = { Toggled = true },
				},

				ui:Button
				{
					Weight = 0,
					ID = "ButtonNested",
					Text = "Nested View",
					Checkable = true,
					AutoExclusive = true,
					MinimumSize = { 100, 1 },
				},

				ui:CheckBox
				{
					Weight = 1,
					ID = "CheckBoxHideEmptyClasses",
					Text = "Hide Classes Without Members",
					Checked = true,
					StyleSheet = [[
                        QCheckBox
                        {
                            margin-left: 8px;
                        }
                    ]],
				},

				ui:Label
				{
					MinimumSize = { 1, 22 }, MaximumSize = { left_pane_size - 215, 22 },
					ID = "LabelStatus",
					Text = "",
					Alignment = { AlignVCenter = true, AlignRight = true },
				},
			},
		},
	})
	
	local size_policy_flags = { GrowFlag = 1, ExpandFlag = 2, ShrinkFlag = 4, IgnoreFlag = 8 }
	local size_policy =
	{
		Fixed = 0,
		Minimum = size_policy_flags.GrowFlag,
		Maximum = size_policy_flags.ShrinkFlag,
		Preferred = size_policy_flags.GrowFlag + size_policy_flags.ShrinkFlag,
		Expanding = size_policy_flags.GrowFlag + size_policy_flags.ShrinkFlag + size_policy_flags.ExpandFlag,
		MinimumExpanding = size_policy_flags.GrowFlag + size_policy_flags.ExpandFlag,
		Ignored = size_policy_flags.ShrinkFlag + size_policy_flags.GrowFlag + size_policy_flags.IgnoreFlag,
	}

	windowItems = window:GetItems()
	windowItems.ClassBrowser:Resize( { 1250, 600 } )

	-- For some reason setting ButtonFlat.Checked = true in the window definition table doesn't work
	-- consistently in Resolve/Fusion v17.4 so we set it here instead
	windowItems.ButtonFlat.Checked = true

	windowItems.TreeFlat:SetFocus()

	-- Shows a status message at the bottom of the window
	local function show_status(message)
		windowItems.LabelStatus.Text = message
	end

	-- Updates the window in case we have switched between flat and nested trees
	local function update_tree_visibility()
		windowItems.CheckBoxHideEmptyClasses.Visible = windowItems.ButtonFlat.Checked
		windowItems.TreeFlat.Hidden = not windowItems.ButtonFlat.Checked
		windowItems.TreeNested.Hidden = windowItems.ButtonFlat.Checked

		windowItems.ClassBrowser:RecalcLayout()
	end
	
	------------------------------------------
	-- Events
	------------------------------------------

	-- Apply/clear filter of the class tree 
	function window.On.LineEditFilter.ReturnPressed(ev)
		local text = windowItems.LineEditFilter.Text
		local tree = iif(windowItems.ButtonFlat.Checked, windowItems.TreeFlat, windowItems.TreeNested)
		local hide = windowItems.CheckBoxHideEmptyClasses.Checked and windowItems.CheckBoxHideEmptyClasses.Visible

		show_status("Filtering, please wait...")
		tree.UpdatesEnabled = false
		
		if (#text == 0) then
			set_item_visibility(tree, classes, hide)
		else
			deselect_items(tree)
				
			-- Hide all items
			for i, item in ipairs(get_all_items(tree)) do
				if (not item.Hidden) then
					item.Hidden = true
				end
			end
		
			-- Unhide found items and their parents
			for i, foundItem in ipairs(find_items(tree, text)) do
				local stack = table.pack(foundItem)
		
				while (#stack > 0) do
					local item = table.remove(stack)
					local class = item.Text[0]

					if (item.Hidden and (classes[class].has_members or not hide)) then
						item.Hidden = false
						item.Expanded = true
					end
		
					local parentItem = item:Parent()
		
					if (parentItem) then
						table.insert(stack, parentItem)
					end
				end
			end

			is_filtered = true
		end
		
		show_status("")
		tree.UpdatesEnabled = true
	end

	-- Hide/unhide items
	function window.On.CheckBoxHideEmptyClasses.Clicked(ev)
		show_status("Please wait...")
		windowItems.LineEditFilter.Text = ""
		set_item_visibility(windowItems.TreeFlat, classes, ev.On)
		show_status("")
	end
	
	-- Switch between flat/nested tree
	function window.On.ButtonFlat.Toggled(ev)
		local tree = iif(ev.On, windowItems.TreeFlat, windowItems.TreeNested)

		if (tree and tree:TopLevelItemCount() > 0) then
			show_status("Please wait...")
			windowItems.ClassBrowser.UpdatesEnabled = false
			
			local other_tree = iif(not ev.On, windowItems.TreeFlat, windowItems.TreeNested)
			local other_tree_selected_items = other_tree:SelectedItems()
			local current_class_name = nil
		
			if (other_tree_selected_items and #other_tree_selected_items > 0) then
				current_class_name = other_tree_selected_items[1].Text[0]
			end

			if (is_filtered) then
				windowItems.LineEditFilter.Text = ""
				set_item_visibility(other_tree, classes, windowItems.CheckBoxHideEmptyClasses.Checked and windowItems.CheckBoxHideEmptyClasses.Visible)
			end

			update_tree_visibility()
			deselect_items(tree)
		
			if (not current_class_name or not select_item(tree, current_class_name)) then
				select_item(tree, get_first_visible_item(tree).Text[0])
			end
		
			show_status("")
			windowItems.ClassBrowser.UpdatesEnabled = true
		end
	end

	-- Displays the selected class as HTML (or clears the HTML)
	local function display_selected_class(selected_items)
		if (selected_items and #selected_items > 0) then
			if (selected_items[1].Text[0] ~= last_displayed_class) then
				display_class(selected_items[1].Text[0])
			end
		else
			windowItems.TextEditHelp.HTML = ""
			last_displayed_class = ""
		end
	end
	
	-- Event triggered when selecting a class in the flat tree
	function window.On.TreeFlat.ItemSelectionChanged(ev)
		display_selected_class(ev.sender:SelectedItems())
	end

	-- Event triggered when selecting a clas in the nested tree
	function window.On.TreeNested.ItemSelectionChanged(ev)
		display_selected_class(ev.sender:SelectedItems())
	end

	-- Navigate to anchors or to external links
	local function navigate_to(ev)
		if (ev.URL:sub(1,1) == "#") then
			-- Go to an anchor tag on the same "page"	
		
			local anchor = ev.URL:sub(2)
			ev.sender:ScrollToAnchor(anchor)

			log("Scrolled to anchor: "..anchor, "verbose")
		else
			-- Open another class in the tree
			local url_parts = split(ev.URL, "://")
			
			if (url_parts and #url_parts > 1 and url_parts[1] == "displayclass") then
				local class_name_and_anchor = split(url_parts[2], "#")
				local class_name = class_name_and_anchor[1]
				local anchor = class_name_and_anchor[2]
				local tree = iif(windowItems.ButtonFlat.Checked, windowItems.TreeFlat, windowItems.TreeNested)

				deselect_items(tree)

				if (is_filtered) then
					show_status("Please wait...")
					windowItems.LineEditFilter.Text = ""
					set_item_visibility(tree, classes, windowItems.CheckBoxHideEmptyClasses.Checked)
					show_status("")
				end

				select_item(tree, class_name)
				display_class(class_name)

				if (anchor) then
					ev.sender:ScrollToAnchor(anchor)
					tree:Update()

					log("Scrolled to anchor: "..anchor, "verbose")
				end
			else
				if (ffi.os == "Windows") then
					os.execute(string.format("start /MIN powershell.exe -Command \"& { rundll32 url,OpenURL '%s' }\"", ev.URL))
				elseif (ffi.os == "OSX") then
					os.execute(string.format("open \"%s\" &", ev.URL))
				else
					os.execute(string.format("xdg-open \"%s\" &", ev.URL))
				end
			end
		end
	end

	-- Clicked links in the header HTML (not available in Fusion 9)
	function window.On.TextEditHeader.AnchorClicked(ev)
		navigate_to(ev)
	end

	-- Clicked links in the Help HTML (not available in Fusion 9)
	function window.On.TextEditHelp.AnchorClicked(ev)
		navigate_to(ev)
	end

	function window.On.FolderButton.Clicked(ev)
		ev.URL = script_file.Path
		navigate_to(ev)
	end

	function window.On.AboutButton.Clicked(ev)
		ev.URL = "https://tiny.cc/classbrowser"
		navigate_to(ev)
	end

	function window.On.ClassBrowser.Close(ev)
		dispatcher:ExitLoop()
	end

	return window, windowItems
end

-- Creates the splash window
local function create_splash_window()
	local splash_window = dispatcher:AddWindow(
	{
		ID = "Splash",
		Margin = 0,
		Spacing = 0,
		WindowFlags = { SplashScreen = true },
		Events = { UpdateProgress = true, ReName = true },

		ui:VGroup
		{
			ui:Label
			{	
				Weight = 0,
				Text = script_name.." for DaVinci Resolve/Fusion",
				Alignment = { AlignCenter = true },
				StyleSheet = "color: white; font-weight: bold; font-size: 14px; margin-top: 40px;",
			},
			
			ui:Label
			{
				ID = "Title",
				Text = "Creating Awesome Stuff",
				Alignment = { AlignCenter = true },
			},
		},

		ui:Label
		{
			ID = "SplashProgress",
			StyleSheet = "max-height: 1px; background-color: rgb(102, 0, 39);",
		},

		ui:Label
		{
			ID = "SplashBorder",
			StyleSheet = "border: 1px solid black;",
		},
	})

	local splash_window_items = splash_window:GetItems()

	splash_window_items.Splash.UpdatesEnabled = false

	splash_window_items.Splash:Resize( {400, 200} )
	splash_window_items.SplashBorder:Resize( {400, 200} )
	splash_window_items.SplashBorder:Lower()
	splash_window_items.SplashProgress:Move( { 50, 100 } )

	splash_window_items.Splash.UpdatesEnabled = true

	function splash_window.On.Splash.UpdateProgress(ev)
		local label = splash_window_items.SplashProgress
		label:Resize( {ev.Progress * 3, 2})

		label.StyleSheet = label.StyleSheet:gsub("background%-color: rgb%(102, (%d+), 39%);", "background-color: rgb(102, "..math.floor(ev.Progress * 2.21)..", 39);")
	end

	function splash_window.On.Splash.ReName(ev)
		local label = splash_window_items.Title
		label:SetText(ev.Title)
	end

	return splash_window, splash_window_items
end

-- Sends an event to the splash window containing progress information
local function update_progress(progress, iterations, title)
	app.UIManager:QueueEvent(splash_items.Splash, "UpdateProgress", { Progress = progress } )

	if (title) then
		app.UIManager:QueueEvent(splash_items.Splash, "ReName", { Title = title } )
	end
	
	-- Might want to give more time to the events at certain times
	if (not iterations) then iterations = 1 end
	for i = 1, iterations do
		dispatcher:StepLoop()
	end
end

function tableToJson(table, file)
    local file_handle = io.open(file, "w")
    file_handle:write(json.encode(table, { indent = true }))
    file_handle:close()
end

function sortTableBySubTable(t, name)
    table.sort(t, function(a, b)
        return a[name] < b[name]
    end)
    return t
end

function createMarkdown(class_name)
	local out = io.open(docsify_location..class_name:gsub(" ", "_")..".md", "w")

	local temp = ""

	--[[ SORT ALL LISTS ]]--
	for i,j in pairs(propertiesList) do
		j["items"] = sortTableBySubTable(j["items"], "name")
	end

	for i,j in pairs(methodList) do
		j["items"] = sortTableBySubTable(j["items"], "name")
	end

	if #tagsList > 0 then
		tagsList = sortTableBySubTable(tagsList, "method")
		for i,j in pairs(tagsList) do
			j["tags"] = sortTableBySubTable(j["tags"], "value")
		end
	end

	if #registryList > 0 then
		registryList = sortTableBySubTable(registryList, "full_name")
	end

	--[[ Header ]]--
	out:write("# "..headerList["name"].."\n")
	if headerList["short_help"] ~= nil and headerList["short_help"] ~= "" then
		out:write(headerList["short_help"].."\n")
	end
	if headerList["qt"] ~= nil then
		out:write("Qt: ["..headerList["qt"]["name"].."]("..headerList["qt"]["url"]..")")
		out:write("\n\n")
	end
	if headerList["short_help"] ~= nil and headerList["short_help"] ~= "" then
		out:write(headerList["short_help"])
		out:write("\n\n")
	end
	if headerList["class_inheritance"] ~= nil then
		for i,v in ipairs(headerList["class_inheritance"]) do
			out:write(" : ["..v.."]("..v:gsub(" ", "_")..".md)")
		end
		out:write("\n")
	end

	out:write("___\n")

	--[[ Object list ]]--
	for i,j in pairs(propertiesList) do
		out:write("### "..j["header"].."  \n")

		if j["info_text"] ~= nil and j["info_text"] ~= "" then
			out:write(""..j["info_text"].."  \n")
		end
		out:write("> [!NOTE|labelVisibility:hidden|iconVisibility:hidden]\n")
		for k,v in pairs(j["items"]) do
			out:write("> ["..v["name"].."](#"..v["name"]..")\n")
			out:write(">\n")
		end
	end

	for i,j in pairs(methodList) do
		out:write("### "..j["header"].."  \n")
		if j["info_text"] ~= nil and j["info_text"] ~= "" then
			out:write(j["info_text"].."  \n")
		end
		out:write("> [!TIP|labelVisibility:hidden|iconVisibility:hidden]\n")
		for k,v in pairs(j["items"]) do
			out:write("> ["..v["name"].."](#"..v["name"]..")()\n")
			out:write(">\n")
		end
	end

	if #tagsList > 0 then
		out:write("### Tag Map\n")
		for i,j in pairs(tagsList) do
			if j["method"] ~= nil then
				out:write("> "..j["method"].."\n")
				out:write(">\n")
			end
			out:write(">> [!ATTENTION|labelVisibility:hidden|iconVisibility:hidden]\n")
			for k,v in ipairs(j["tags"]) do
				out:write(">> ["..v["value"].."](#"..v["value"]..")\n")
				out:write(">>\n")
			end
		end
	end

	if #registryList > 0 then
		out:write("### Registry Attributes\n")
		for i,j in pairs(registryList) do
			out:write("> ["..j["full_name"].."](#"..j["full_name"]..")\n")
			out:write(">\n")
		end
	end

	out:write("___\n")

	--[[ Properties ]]--
	for i,j in pairs(propertiesList) do
		out:write("\n# "..j["header"]..": <!-- {docsify-ignore} -->\n\n")
		for k,v in pairs(j["items"]) do
			out:write("### "..v["name"].."\n")
			out:write("> [!NOTE|labelVisibility:hidden|iconVisibility:hidden]\n")

			if v["short_help"] ~= "" then
				out:write("> "..v["short_help"].."\n")
				out:write(">\n")
			end

			if v["return_type"] ~= "" then
				out:write("> `"..v["return_type"].."`\n")
				out:write(">\n")
			end

			if v["access_class"] ~= "" then
				if v["access_class"] == "read_only" then
					temp = "Read Only"
				elseif v["access_class"] == "read_write" then
					temp = "Read/Write"
				elseif v["access_class"] == "write_only" then
					temp = "Write Only"
				end
				out:write("> *<span class=\""..v["access_class"].."\">"..temp.."</span>*\n")
				out:write(">\n")
			end

			if v["description"] ~= "" then
				out:write("> ```\n")
				out:write(v["description"]:gsub("\"", "`").."\n")
				out:write("> ```\n")
				out:write(">\n")
			end

			if #v["see_also"] > 0 then
				temp = ""
				for m,n in ipairs(v["see_also"]) do
					temp = temp.."["..n["name"].."]("
					if n["property"] ~= nil then
						temp = temp..n["property"]:gsub(" ", "_")..".md"
					end
					temp = temp.."#"..n["name"]..")"
					if m ~= #v["see_also"] then
						temp = temp..", "
					end
				end
				out:write("> *Se also: "..temp.."*\n")
			end

			out:write("___\n\n")

		end
	end

	--[[ Methods ]]--
	for i,j in pairs(methodList) do
		out:write("\n# "..j["header"]..": <!-- {docsify-ignore} -->\n\n")
		for k,v in pairs(j["items"]) do
			out:write("### "..v["name"].."()\n")
			out:write("> [!TIP|labelVisibility:hidden|iconVisibility:hidden]\n")

			if v["short_help"] ~= "" then
				out:write("> "..v["short_help"].."\n")
				out:write(">\n")
			end
			
			for m,n in pairs(v["usage"]) do
				out:write("> ```php\n")
				out:write(n.."\n")
				out:write("> ```\n")
				out:write(">\n")
			end

			if v["description"] ~= "" then
				out:write("> ```\n")
				out:write(v["description"]:gsub("\"", "`").."\n")
				out:write("> ```\n")
				out:write(">\n")
			end

			if #v["see_also"] > 0 then
				temp = ""
				for m,n in ipairs(v["see_also"]) do
					temp = temp.."["..n["name"].."()]("
					if n["method"] ~= nil then
						temp = temp..n["method"]:gsub(" ", "_")..".md"
					end
					temp = temp.."#"..n["name"]..")"
					if m ~= #v["see_also"] then
						temp = temp..", "
					end
				end
				out:write("> *Se also: "..temp.."*\n")
			end
			
			out:write("___\n\n")
		end
	end

	--[[ Tag Map ]]--
	if #tagsList > 0 then
		out:write("\n# Tag Map: <!-- {docsify-ignore} -->\n\n")
	end
	for i,j in pairs(tagsList) do

		if j["method"] ~= nil then
			out:write(">## "..j["method"].." \n")
		end
		if j["parent_tag"] ~= nil then
			out:write("> : ["..j["parent_tag"].."]("..j["parent_tag"]:gsub("%.", ".md#"):gsub(" ", "_")..")\n")
		end

		for k,l in ipairs(j["tags"]) do
			out:write(">### "..l["value"].."\n")
			out:write(">> [!ATTENTION|labelVisibility:hidden|iconVisibility:hidden]\n")

			if l["key_type"] ~= nil and l["key_type"] ~= "" then
				out:write(">> `Type: "..l["key_type"].."`\n")
				out:write(">>\n")
			end

			if l["enum_value"] ~= nil and #l["enum_value"] > 0 then
				out:write(">> Possible "..l["enum_name"].." values\n")
				for i,n in ipairs(l["enum_value"]) do
					out:write(">> - "..n.."\n")
				end
				out:write(">>\n")
			end
		end
		
		out:write("___\n\n")
	end

	--[[ Registry Attributes ]]--
	if #registryList > 0 then
		out:write("\n# Registry Attributes: <!-- {docsify-ignore} -->\n\n")
	end
	for i,j in pairs(registryList) do
		out:write("### "..j["full_name"].."\n")
		out:write("> [!WARNING|labelVisibility:hidden|iconVisibility:hidden]\n")
		
		if j["value"] ~= "" then
			out:write("> `Type: "..j["value"].."`\n")
			out:write(">\n")
		end

		if j["type"] ~= "" then
			out:write("> "..j["type"].."\n")
			out:write(">\n")
		end
		
		out:write("___\n\n")
	end
	
	out:close()
end

function get_table_length(tbl)
	local table_length = 0
	
	if (tbl) then
		for _, __ in pairs(tbl) do
			table_length = table_length + 1
		end
	end
	
	return table_length
end

function createPythonDocs(class_name)
	pythonDocs = {}

	local temp = ""

	--[[ SORT ALL LISTS ]]--
	for i,j in pairs(propertiesList) do
		j["items"] = sortTableBySubTable(j["items"], "name")
	end

	for i,j in pairs(methodList) do
		j["items"] = sortTableBySubTable(j["items"], "name")
	end

	if #tagsList > 0 then
		tagsList = sortTableBySubTable(tagsList, "method")
		for i,j in pairs(tagsList) do
			j["tags"] = sortTableBySubTable(j["tags"], "value")
		end
	end

	if #registryList > 0 then
		registryList = sortTableBySubTable(registryList, "full_name")
	end

	--[[ Header ]]--
	pythonDocs["name"] = headerList["name"]
	if headerList["short_help"] ~= nil and headerList["short_help"] ~= "" then
		pythonDocs["short_help"] = headerList["short_help"]
	end
	if headerList["qt"] ~= nil then
		pythonDocs["qt"] = headerList["qt"]["name"]
	end
	if headerList["class_inheritance"] ~= nil then
		local list = {}
		for i,v in ipairs(headerList["class_inheritance"]) do
			list[#list+1] = v
		end
		pythonDocs["class_inheritance"] = list
	end

	--[[ Properties ]]--
	if #propertiesList > 0 then
		pythonDocs["properties"] = {}
	end
	for i,j in pairs(propertiesList) do
		pythonDocs["properties"]["header_text"] = j["header"]
		if j["info_text"] ~= nil and j["info_text"] ~= "" then
			pythonDocs["properties"]["info_text"] = j["info_text"]
		end
		for k,v in pairs(j["items"]) do
			pythonDocs["properties"][v["name"]] = {}

			if v["short_help"] ~= "" then
				pythonDocs["properties"][v["name"]]["short_help"] = v["short_help"]
			end

			if v["return_type"] ~= "" then
				pythonDocs["properties"][v["name"]]["return_type"] = v["return_type"]:gsub("Type: ", "")
			end

			if v["access_class"] ~= "" then
				if v["access_class"] == "read_only" then
					temp = "Read Only"
				elseif v["access_class"] == "read_write" then
					temp = "Read/Write"
				elseif v["access_class"] == "write_only" then
					temp = "Write Only"
				end
				pythonDocs["properties"][v["name"]]["access_class"] = temp
			end

			if v["description"] ~= "" then
				pythonDocs["properties"][v["name"]]["description"] = v["description"]
			end

			if #v["see_also"] > 0 then
				temp = ""
				for m,n in ipairs(v["see_also"]) do
					temp = temp.."["..n["name"].."]("
					if n["property"] ~= nil then
						temp = temp..n["property"]:gsub(" ", "_")..".md"
					end
					temp = temp.."#"..n["name"]..")"
					if m ~= #v["see_also"] then
						temp = temp..", "
					end
				end
				pythonDocs["properties"][v["name"]]["see_also"] = temp
			end
		end
	end

	--[[ Methods ]]--
	if #methodList > 0 then
		pythonDocs["methods"] = {}
	end
	for i,j in pairs(methodList) do
		pythonDocs["methods"]["header_text"] = j["header"]
		if j["info_text"] ~= nil and j["info_text"] ~= "" then
			pythonDocs["methods"]["info_text"] = j["info_text"]
		end
		for k,v in pairs(j["items"]) do
			pythonDocs["methods"][v["name"]] = {}

			if v["short_help"] ~= "" then
				pythonDocs["methods"][v["name"]]["short_help"] = v["short_help"]
			end
			
			if #v["usage"] > 0 then
				pythonDocs["methods"][v["name"]]["usage"] = {}
			end
			for m,n in pairs(v["usage"]) do
				temp = n:gsub(headerList["name"]..":", ":")
				pythonDocs["methods"][v["name"]]["usage"][#pythonDocs["methods"][v["name"]]["usage"]+1] = temp
			end

			if v["description"] ~= "" then
				pythonDocs["methods"][v["name"]]["description"] = v["description"]
			end

			if #v["see_also"] > 0 then
				temp = ""
				for m,n in ipairs(v["see_also"]) do
					temp = temp.."["..n["name"].."()]("
					if n["method"] ~= nil then
						temp = temp..n["method"]:gsub(" ", "_")..".md"
					end
					temp = temp.."#"..n["name"]..")"
					if m ~= #v["see_also"] then
						temp = temp..", "
					end
				end
				pythonDocs["methods"][v["name"]]["see_also"] = temp
			end
		end
	end

	--[[ Registry Attributes ]]--
	if #registryList > 0 then
		pythonDocs["attributes"] = {}
	end
	for i,j in pairs(registryList) do
		pythonDocs["attributes"][j["full_name"]] = {}
		
		if j["value"] ~= "" then
			pythonDocs["attributes"][j["full_name"]]["value"] = j["value"]
		end

		if j["type"] ~= "" then
			pythonDocs["attributes"][j["full_name"]]["type"] = j["type"]
		end
	end
	local out = io.open(docsify_location..class_name:gsub(" ", "_")..".json", "w")
	
	out:write(clean(json.encode(pythonDocs)))
	out:close()

end

-- Controller for initialization tasks, progress updates are sent from here
local function initialize()
	local steps = 100 / 6

	splash_window, splash_items = create_splash_window()
	splash_window:Show()

	local maps = load_maps(runtime_version)

	tag_map = maps.TagMap
	enum_map = maps.EnumMap
	discovered_class_methods = maps.Methods
	discovered_class_properties = maps.Properties
	classes = get_classes()

	local steps = 100 / 6
	
	update_progress(1 * steps)

	update_classes(classes, discovered_class_methods, discovered_class_properties, tag_map)
	update_classes(classes, added_class_members.Methods, added_class_members.Properties, nil) 

	window, windowItems = create_window()
	update_progress(2 * steps)

	populate_flat_tree(windowItems.TreeFlat, classes)
	update_progress(3 * steps)

	set_item_visibility(windowItems.TreeFlat, classes, windowItems.CheckBoxHideEmptyClasses.Checked)
	update_progress(4 * steps, 2)

	get_children(classes)
	update_progress(5 * steps, 2)
	
	populate_nested_tree(windowItems.TreeNested, classes)
	update_progress(6 * steps, 2)

	registry_index = get_registry()
	update_progress(6 * steps, 2) -- Setting step 6 twice makes it more likely that we have had time to draw the progress bar at 100%

	-- Loop through all classes and generate all .MD files
	sidebar = io.open(docsify_location.."_sidebar.md", "w")
	sidebar:write("<!-- docs/_sidebar.md -->\n")
	sidebar:write("- [Home](/)\n")
	start_time = os.time()
	class_names = {}
	for _, class in ipairs(classes) do
		if hide_classes_without_members == false or class.has_members then
			class_names[#class_names+1] = class.name
		end
	end

	-- Sort alphabetically
	table.sort(class_names, function(a, b) return a:upper() < b:upper() end)

	local steps = 100 / (#class_names + 6)
	
	for i, name in pairs(class_names) do
		display_class(name)
		sidebar:write("- ["..name.."]("..name:gsub(" ", "_")..".md)\n")
		update_progress(i * steps, 1, "Creating "..name:gsub(" ", "_")..".md")
	end

	sidebar:close()
    end_time = os.time()
    print('Done in: ' .. os.difftime(end_time, start_time) .. 's')

	dispatcher:ExitLoop()
	splash_window:Hide()
end

selectedPath = fu:RequestDir('')
if (selectedPath) then 
	docsify_location = tostring(selectedPath)
	initialize()

	window:Show()
	dispatcher:RunLoop()
	window:Hide()

	collectgarbage()
end