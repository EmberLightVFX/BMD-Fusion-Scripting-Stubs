----------------------------------------------------------------------------
-- Based on Roger Magnusson's Class Browser 1.3 for DaVinci Resolve/Fusion v16+ (and Fusion v9)
--
-- v1.0 2024-12-28:
-- * Initial release
--
----------------------------------------------------------------------------

-- Imports
local json = require("dkjson")

-- Options
local script_name = "Generate Maps"
local verbose_log = true


-- Globals
local classes = {}
local tag_map = {}
local enum_map = {}
local discovered_class_methods = {}
local discovered_class_properties = {}
local registry_index = {}
local class_type_index = {}

local runtime_version = app:GetVersion()
if (not runtime_version.App) then -- For Fusion 9 compatibility
    runtime_version.App = "Fusion"
end

-- The attribute descriptions are from the Fusion 8 Scripting Guide:
-- https://documents.blackmagicdesign.com/UserManuals/Fusion8_Scripting_Guide.pdf
-- We'll use these as tooltips when listing attributes
local registry_attribute_descriptions =
{
    REGS_Name = "Specifies the full name of the class represented by this registry entry.",
    REGS_ScriptName =
        "Specifies the scripting name of the class represented by this registry entry.\n" ..
        "If not specified, the full name defined by REGS_Name is used.",
    REGS_HelpFile = "The help file and ID for the class.",
    REGI_HelpID = "The help file and ID for the class.",
    REGS_HelpTopic = "The help file and ID for the class.", -- Was REGI_HelpTopicID in the Scripting Guide
    REGS_OpIconString = "Specifies the toolbar icon text used to represent the class.",
    REGS_OpDescription = "Specifies a description of the class.",
    REGS_OpToolTip = "Specifies a tooltip for the class to provide a longer name or description.",
    REGS_Category = "Specifies the category for the class, defining a position in the Tools menu for tool classes.",
    REGI_ClassType = "Specifies the type of this class, based on the class type constants.",
    REGI_ClassType2 = "Specifies the type of this class, based on the class type constants.",
    REGS_ID = "A unique ID for this class.",                                                  -- Was REGI_ID in the Scripting Guide
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
    REGB_Unpredictable =
        "Indicates if this tool class is predictable or not. Predictable tools will\n" ..
        "generate the same result given the same set of input values, regardless of time.",
    REGI_InputDataType = "Specifies a data type RegID dealt with by the main inputs of this class.",
    REGB_OperatorControl = "Indicates if this tool class provides custom overlay control handling.",
    REGB_Source_GlobalCtrls = "Indicates if this source tool class has global range controls.",
    REGB_Source_SizeCtrls = "Indicates if this source tool class has image resolution controls.",
    REGB_Source_AspectCtrls = "Indicates if this source tool class has image aspect controls.",
    REGB_NoAutoProxy = "Indicates if this tool class does not want things to be auto proxied when it is adjusted.",
    REGI_Logo = "Specifies a resource ID of a company logo for this class.",
    REGI_Priority = "Specifies the priority of this class on the registry list.",
    REGB_NoBlendCtrls = "Indicates if this tool class does not have blend controls.",
    REGB_NoObjMatCtrls = "Indicates if this tool class does not have Object/Material selection controls.",
    REGB_NoMotionBlurCtrls = "Indicates if this tool class does not have Motion Blur controls.",
    REGB_NoAuxChannels =
    "Indicates if this tool class cannot deal with being given Auxiliary channels (such as Z, ObjID, etc)",
    REGB_EightBitOnly =
    "Indicates if this tool class cannot deal with being given greater than 8 bit per channel images.",
    REGB_ControlView = "Indicates if this class is a control view class.",
    REGB_NoSplineAnimation = "Specifies that this data type (parameter class) cannot be animated using a spline.",
    REGI_MergeDataType = "Specifies what type of data this merge tool class is capable of merging.",
    REGB_ForceCommonCtrls = "Forces the tool to have common controls like motion blur, blend etc, even on modifiers.",
    REGB_Particle_ProbabilityCtrls =
    "Specifies that particle tools should have (or not have) various standard sets of controls.",
    REGB_Particle_SetCtrls = "Specifies that particle tools should have (or not have) various standard sets of controls.",
    REGB_Particle_AgeRangeCtrls =
    "Specifies that particle tools should have (or not have) various standard sets of controls.",
    REGB_Particle_RegionCtrls =
    "Specifies that particle tools should have (or not have) various standard sets of controls.",
    REGB_Particle_RegionModeCtrls =
    "Specifies that particle tools should have (or not have) various standard sets of controls.",
    REGB_Particle_StyleCtrls =
    "Specifies that particle tools should have (or not have) various standard sets of controls.",
    REGB_Particle_EmitterCtrls =
    "Specifies that particle tools should have (or not have) various standard sets of controls.",
    REGB_Particle_RandomSeedCtrls =
    "Specifies that particle tools should have (or not have) various standard sets of controls.",
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
	local print_verbose_log = ]] .. tostring(verbose_log) .. [[

	if ((log_type == "verbose" and print_verbose_log) or log_type ~= "verbose") then
		print(str)
	end
end
]]

-- Members to add manually, can be for existing classes or new classes

local added_class_members =
{
    Classes =
    {
        GalleryStill =
        {
            ShortHelp =
            "This class does not provide any API functions but the object type is used by functions in other classes."
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
                        Text =
                        "PageName: \"media\"\n          \"cut\"\n          \"edit\"\n          \"fusion\"\n          \"color\"\n          \"fairlight\"\n          \"deliver\"\n\nReturns: true if the operation was successful"
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
                        Text =
                        "Returns one of: \"media\"\n                \"cut\"\n                \"edit\"\n                \"fusion\"\n                \"color\"\n                \"fairlight\"\n                \"deliver\""
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
                        Text =
                            "The optional argument 'presetName' specifies how the preset shall be named. " ..
                            "If not specified, the preset is named based on the filename.\n\n" ..
                            "Returns: true if the operation was successful"
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
                        Text =
                            "TrackType: \"audio\"\n" ..
                            "           \"video\"\n" ..
                            "           \"subtitle\"\n\n" ..
                            "AudioTrackType: \"mono\"\n" ..
                            "                \"stereo\"\n" ..
                            "                \"5.1film\"\n" ..
                            "                \"7.1film\"\n" ..
                            "                \"adaptive\"\n\n" ..
                            "Returns: true if the operation was successful"
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
                        Text =
                        "TrackType: \"audio\"\n           \"video\"\n           \"subtitle\"\n\nIndex is 1 to GetTrackCount(trackType)\n\nReturns: true if the operation was successful"
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
                        Text =
                        "TrackType: \"audio\"\n           \"video\"\n           \"subtitle\"\n\nIndex is 1 to GetTrackCount(trackType)"
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
                        Text =
                        "TrackType: \"audio\"\n           \"video\"\n           \"subtitle\"\n\nIndex is 1 to GetTrackCount(trackType)"
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
                        Text =
                        "TrackType: \"audio\"\n           \"video\"\n           \"subtitle\"\n\nIndex is 1 to GetTrackCount(trackType)\n\nReturns: true if the operation was successful"
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
                        Text =
                        "TrackType: \"audio\"\n           \"video\"\n           \"subtitle\"\n\nIndex is 1 to GetTrackCount(trackType)\n\nReturns: true if the operation was successful"
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

        -- Method documentation that was available in Resolve v16, but removed in v17
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
                        Text =
                            "Arguments: action - name of action to perform (string)\n" ..
                            "           param1 - (optional) parameter for action (string or int)\n" ..
                            "           param2 - (optional) parameter for action (string or int)\n" ..
                            "           param3 - (optional) parameter for action (string or int)\n\n" ..
                            "Returns: success - true if the action was performed"
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
                        Text =
                        "Arguments: moduleID    - Module Type\n           moduleIndex - index of module\n           parameterID - Parameter Identifier\n           targetModifier - (optional)\n           quiet       - (optional)\n\nReturns: integer or text parameter result"
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
                        Text =
                        "Arguments: moduleID    - Module Type\n           moduleIndex - index of module\n           parameterID - Parameter Identifier\n           value       - Parameter value (integer or text)\n           targetModifier - (optional)\n\nReturns: boolean true if success"
                    }
                ),
                SeeAlso = {}
            }
        )
    }
}

local function mergeTables(...)
    local mergedTable = {}
    for _, tbl in ipairs({ ... }) do
        for _, value in ipairs(tbl) do
            table.insert(mergedTable, value)
        end
    end
    return mergedTable
end

-- Counts the occurrences of the given pattern in a string
local function count(text, pattern)
    return select(2, text:gsub(pattern, ""))
end


local function generate_maps(version)
    local fusion_path

    if (version.App == "Resolve" or version[1] >= 16) then
        fusion_path = app:MapPath("FusionLibs:")
    else
        -- Fusion 9
        fusion_path = app:MapPath("Fusion:")
    end

    local temp_folder

    if (ffi.os == "Windows") then
        temp_folder = os.getenv("TEMP") .. "\\"
    else
        temp_folder = os.getenv("TMPDIR")

        if (ffi.os == "Linux" and not temp_folder) then
            temp_folder = "/tmp/"
        end
    end

    local plugins_folder = "Plugins"

    if (version.App == "Fusion" and ffi.os == "Windows" and version[1] <= 18) then
        plugins_folder = plugins_folder .. [[\Blackmagic]]
    end

    local filename = temp_folder .. version.App .. "_Class_Browser.luatable"

    if (bmd.fileexists(filename)) then
        assert(os.remove(filename))
    end


    -- Get the data in a context where EnumMap, TagMap and functions aren't limited as they are when used in scripts after Fusion ~8
    local mainCode = [===[
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
                Windows = [[]===] .. plugins_folder .. [===[\fuses.plugin]],
                OSX = [[]===] .. plugins_folder .. [===[/fuses.plugin]],
                Linux = [[]===] .. plugins_folder .. [===[/fuses.plugin]],
            },
            {
                Windows = [[]===] .. plugins_folder .. [===[\text.plugin]],
                OSX = [[]===] .. plugins_folder .. [===[/text.plugin]],
                Linux = [[]===] .. plugins_folder .. [===[/text.plugin]],
            }
        )

        for i = 1, fusion_filenames.n do
            fusion_filenames[i].Windows = [[]===] .. fusion_path .. [===[]]..fusion_filenames[i].Windows
            fusion_filenames[i].OSX = [[]===] .. fusion_path .. [===[]]..fusion_filenames[i].OSX
            fusion_filenames[i].Linux = [[]===] .. fusion_path .. [===[]]..fusion_filenames[i].Linux
        end

        local ffi_prefix = " ffi_"
        local split = loadstring([[]===] .. split_function .. [===[]])()
        local trim = loadstring([[]===] .. trim_function .. [===[]])()
        local log = loadstring([[]===] .. log_function .. [===[]])()

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
    ]===]

    local fileWriteCommand = string.format([[
        local data = {
            Script = "%s",
            AppVersion = app:GetVersion(),
            EnumMap = EnumMap,
            TagMap = TagMap,
            Methods = members.Methods,
            Properties = members.Properties
        }

        -- Write the Lua table
        bmd.writefile("%s", data)
    ]], script_name, filename:gsub("\\", "\\\\"))

    app:Execute(mainCode .. fileWriteCommand)

    local wait_start = os.time()
    local timeout = 15 -- seconds

    -- Declare a sleep function available in the OS (we can't use Fusion():Sleep() because it sleeps the thread we want to wait for)
    ffi.cdef [[ void Sleep(int ms); int poll(struct pollfd *fds,unsigned long nfds,int timeout); ]]
    local sleep = iif(ffi.os == "Windows", function(milliseconds) ffi.C.Sleep(milliseconds) end,
        function(milliseconds) ffi.C.poll(nil, 0, milliseconds) end)

    -- Wait until the file has been written
    while (not bmd.fileexists(filename)) do
        if (os.time() - wait_start >= timeout) then
            error(string.format("Timeout waiting for data file: \"%s\"", filename))
        end

        sleep(200) -- milliseconds
    end

    return bmd.readfile(filename)
end


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
            if i == 1 then
                print("Exists")
            end
            --log("Duplicate class name found: "..class_name)
            -- Duplicates don't matter in practice since GetHelpRaw
            -- doesn't seem to be able to tell them apart anyway
            -- (they have the same inheritance path)
        else
            classes[class_name] = classes[i]
        end
    end

    -- Get full inheritance path of each class
    for _, class in ipairs(classes) do
        local stack = table.pack(class)
        local current_path = ""

        -- Build the path by following each parent
        while (#stack > 0) do
            local current_class = table.remove(stack)

            current_path = "/" .. current_class.name .. current_path

            local parent_class = current_class.parent

            if (parent_class) then
                table.insert(stack, classes[parent_class])
            end
        end

        class.path = current_path
    end

    return classes
end

-- Updates the documented classes with info from the TagMap and discovered methods/properties
local function update_classes(classes, class_methods, class_properties, tag_map)
    local function get_tag_map_parent_path(class_name, path)
        if (not path) then
            path = ""
        end

        for _, value in pairs(tag_map[class_name]) do
            if (value.__parent) then
                local parent_class_name = value.__parent:sub(1, value.__parent:find(".", 1, true) - 1)
                return get_tag_map_parent_path(parent_class_name, "/" .. parent_class_name .. path)
            end
        end

        return path
    end

    local function add_missing_classes(tbl, is_tag_map)
        if (tbl) then
            for class_name, _ in pairs(tbl) do
                local class_info = classes[class_name]

                if (not class_info) then
                    local path = "/" .. class_name
                    local parent = nil

                    if (is_tag_map) then
                        path = get_tag_map_parent_path(class_name) .. "/" .. class_name
                        local path_parts = split(path, "/")
                        local root_class = classes[path_parts[2]]

                        -- Reassign to the true root class if it exists
                        if (root_class and count(root_class.path, "/") >= 2) then
                            path = root_class.path .. "/" .. table.concat({ select(3, table.unpack(path_parts)) }, "/")
                        end

                        parent = path_parts[#path_parts - 1]

                        if (#parent == 0) then
                            parent = nil
                        end
                    end

                    classes[#classes + 1] =
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

-- Creates HTML and adds it to the TextEdit widgets
local function generate_class_data(class_name)
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
            attribute_type = "[unknown] (\"" .. attribute_type .. "\")"
        end

        return attribute_type, attribute_name_only
    end

    local function get_attribute_value_clean(value)
        if (type(value) == "table") then
            local output = dumptostring(value)
            output = output:gsub("\\n", "\n") -- Fix for Fusion 9 bug in dumptostring()

            return tostring(output:sub(output:find("\n") + 1, 1, true))
        else
            return tostring(value)
        end
    end

    local function display_tags(class_name, tagsList)
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
                print("Unknown type: " .. type_name)
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
        if tags then
            for method, method_tags in pairs(tags) do
                local tag_entry = {
                    method = method,
                    parent_tag = nil,
                    tags = {}
                }

                for key, value in pairs(method_tags) do
                    if key == "__parent" then
                        tag_entry.parent_tag = value
                    end
                end

                for key, value in pairs(get_method_tags(runtime_version, method_tags)) do
                    if type(key) == "number" then
                        local tag_info = get_method_tags_by_value(runtime_version, method_tags, value)
                        tag_entry.tags[#tag_entry.tags + 1] = {
                            value = value,
                            key_type = get_tag_type(tag_info.Type, tag_info.Enum),
                            enum_name = tag_info.Enum and split(tag_info.Enum, ".")[2] or nil,
                            enum_values = tag_info.Enum and get_enum(tag_info.Enum).Values or nil
                        }
                    end
                end
                tagsList[#tagsList + 1] = tag_entry
            end
        end
    end

    local function display_registry(class_name, registryList)
        local reg_attributes = registry_index[class_name]

        if reg_attributes then
            local sorted_attributes = {}

            for key, value in pairs(reg_attributes) do
                -- attribute_type doesn't exists?
                if (#tostring(value) > 0 or attribute_type == "string") then
                    local attribute_type, attribute_name = parse_attribute(key)
                    sorted_attributes[#sorted_attributes + 1] = {
                        Name = attribute_name,
                        FullName = key,
                        Type = attribute_type,
                        Value = value,
                        Tooltip = registry_attribute_descriptions[key] or "",
                        ClassType = nil
                    }

                    -- Handle ClassType special case
                    if key == "REGI_ClassType" then
                        local class_type_by_id = class_type_index[value]
                        if class_type_by_id then
                            sorted_attributes[#sorted_attributes].ClassType = class_type_by_id
                        end
                    end
                end
            end

            table.sort(sorted_attributes, function(a, b) return a.Name < b.Name end)

            for i, attribute in ipairs(sorted_attributes) do
                registryList[i] = {
                    FullName = attribute.FullName,
                    Value = attribute.Type,
                    Type = get_attribute_value_clean(attribute.value),
                    ClassType = attribute.ClassType,
                    Tooltip = attribute.Tooltip
                }
            end
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

    -- Initialize our data collectors
    local tagsList = {}
    local registryList = {}

    -- Process all members
    local variables_help = {}
    local functions_help = {}
    local discovered_properties = copy_members(class_name, discovered_class_properties)
    local discovered_methods = copy_members(class_name, discovered_class_methods)
    local added_properties = copy_members(class_name, added_class_members.Properties)
    local added_methods = copy_members(class_name, added_class_members.Methods)

    if (class_help) then
        if (#class_help.Members > 0) then
            table.sort(class_help.Members)
            for _, member in ipairs(class_help.Members) do
                local member_help = app:GetHelpRaw(class_name, member)
                if (member_help.Type:lower() == "variable") then
                    variables_help[#variables_help + 1] = member_help
                elseif (member_help.Type:lower() == "function") then
                    functions_help[#functions_help + 1] = member_help
                end
            end
        end
    end

    update_existing_members(discovered_properties, variables_help)
    update_existing_members(added_properties, variables_help)
    update_existing_members(discovered_methods, functions_help)
    update_existing_members(added_methods, functions_help)

    display_tags(class_name, tagsList)
    display_registry(class_name, registryList)

    -- Create final data structure
    local classData = {
        Name = class.name,
        Path = class.path,
        Parent = class.parent,
        ShortHelp = class_help and class_help.ShortHelp or "",
        QtInfo = qt_documentation[class_name],
        Properties = mergeTables(variables_help, discovered_properties, added_properties),
        Methods = mergeTables(functions_help, discovered_methods, added_methods),
        Tags = tagsList,
        Registry = registryList
    }

    return classData
end

local function get_registry()
    local registry = {}

    for _, reg in ipairs(app:GetRegList()) do
        if (reg) then
            local reg_attr = reg:GetAttrs()

            if (reg_attr) then
                if (registry[reg_attr.REGS_ID]) then
                    print("Duplicate entry: " .. reg_attr.REGS_ID)
                else
                    registry[reg_attr.REGS_ID] = reg_attr
                end
            end
        end
    end

    return registry
end

local function cleanup_classes(class_list)
    local i = 1
    while i <= #class_list do
        if not class_list[i].methods and not class_list[i].properties then
            table.remove(class_list, i)
        else
            i = i + 1
        end
    end
end

local function cleanup_empty_classes(class_list)
    local i = 1
    while i <= #class_list do
        if #class_list[i].Methods == 0 and #class_list[i].Properties == 0 and #class_list[i].Tags == 0 then
            table.remove(class_list, i)
        else
            i = i + 1
        end
    end
end

local maps = generate_maps(runtime_version)
tag_map = maps.TagMap
enum_map = maps.EnumMap
discovered_class_methods = maps.Methods
discovered_class_properties = maps.Properties
classes = get_classes()

update_classes(classes, discovered_class_methods, discovered_class_properties, tag_map)
update_classes(classes, added_class_members.Methods, added_class_members.Properties, nil)

print("Cleaning up classes")
cleanup_classes(classes)

registry_index = get_registry()
local all_class_data = {}
for class_name, _ in pairs(classes) do
    local class_data = generate_class_data(class_name)
    table.insert(all_class_data, class_data)
end

print("Cleaning up empty classes")
cleanup_empty_classes(all_class_data)

local scriptFolder = arg[0]:match("(.*[/\\])")

local save_file = fu:RequestFile(scriptFolder, runtime_version.App .. "_fusion_stubs.luatable", { FReqB_Saving = true })
local filename = save_file

if (bmd.fileexists(filename)) then
    assert(os.remove(filename))
end
print("Saving luatable")
bmd.writefile(filename, all_class_data)

local json_data = json.encode(all_class_data, { indent = true })
-- Write the JSON data directly to the file
local json_filename = filename:gsub(".luatable", ".json")

if (bmd.fileexists(json_filename)) then
    assert(os.remove(json_filename))
end

local json_file = io.open(json_filename, "w")
if json_file then
    print("Saving JSON")
    json_file:write(json_data)
    json_file:close()
else
    error("Could not open file for writing: " .. json_filename)
end

print("Done!")
