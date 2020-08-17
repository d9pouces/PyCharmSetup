import os
import re
import xml.etree.ElementTree as ET
from typing import Optional


class PyCharmConfig:
    def __init__(self, project_dir: str, module: Optional[str] = None):
        self.project_dir = project_dir
        self.module = module

    def get_default_module(self) -> Optional[str]:
        xml_root = ET.parse(os.path.join(self.project_dir, ".idea", "modules.xml"))
        module = xml_root.find("module")
        if module is None:
            return None
        matcher = re.match(r".*/([^/]+)\.iml$", module.get("filepath") or "")
        if not matcher:
            return None
        return matcher.group(1)

# misc.xml
# <project version="4">
#   <component name="JavaScriptSettings">
#     <option name="languageLevel" value="ES6" />
#   </component>
#   <component name="ProjectRootManager" version="2" project-jdk-name="Python 3.8 (CKDemo)" project-jdk-type="Python SDK" />
# </project>

# watcherTasks.xml
# <?xml version="1.0" encoding="UTF-8"?>
# <project version="4">
#   <component name="ProjectTasksOptions">
#     <TaskOptions isEnabled="true">
#       <option name="arguments" value="$ProjectFileDir$/manage.py config python --filename pycharm.py" />
#       <option name="checkSyntaxErrors" value="true" />
#       <option name="description" />
#       <option name="exitCodeBehavior" value="ERROR" />
#       <option name="fileExtension" value="py" />
#       <option name="immediateSync" value="true" />
#       <option name="name" value="Génération de la config" />
#       <option name="output" value="" />
#       <option name="outputFilters">
#         <array />
#       </option>
#       <option name="outputFromStdout" value="false" />
#       <option name="program" value="$JDKPath$" />
#       <option name="runOnExternalChanges" value="true" />
#       <option name="scopeName" value="Fichiers de config" />
#       <option name="trackOnlyRoot" value="false" />
#       <option name="workingDir" value="$ProjectFileDir$" />
#       <envs />
#     </TaskOptions>
#   </component>
# </project>%

# workspace.xml
# <?xml version="1.0" encoding="UTF-8"?>
# <project version="4">
#   <component name="DjangoConsoleOptions" custom-start-script="import sys; print('Python %s on %s' % (sys.version, sys.platform))&#10;import django; print('Django %s' % django.get_version())&#10;sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])&#10;if 'setup' in dir(django): django.setup()&#10;import django_manage_shell; django_manage_shell.run(PROJECT_ROOT)">
#     <option name="myCustomStartScript" value="import sys; print('Python %s on %s' % (sys.version, sys.platform))&#10;import django; print('Django %s' % django.get_version())&#10;sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])&#10;if 'setup' in dir(django): django.setup()&#10;import django_manage_shell; django_manage_shell.run(PROJECT_ROOT)" />
#   </component>
#   <component name="NamedScopeManager">
#     <scope name="Fichiers de config" pattern="file:local_settings.py||file:df_site/defaults.py||file:metier/defaults.py" />
#   </component>
#   <component name="RunManager" selected="npm.build-prod">
#     <configuration name="Tests" type="DjangoTestsConfigurationType">
#       <module name="CKDemo" />
#       <option name="INTERPRETER_OPTIONS" value="" />
#       <option name="PARENT_ENVS" value="true" />
#       <envs>
#         <env name="PYTHONUNBUFFERED" value="1" />
#       </envs>
#       <option name="SDK_HOME" value="$USER_HOME$/.virtualenvs/CKDemo/bin/python" />
#       <option name="WORKING_DIRECTORY" value="" />
#       <option name="IS_MODULE_SDK" value="false" />
#       <option name="ADD_CONTENT_ROOTS" value="true" />
#       <option name="ADD_SOURCE_ROOTS" value="true" />
#       <EXTENSION ID="PythonCoverageRunConfigurationExtension" runner="coverage.py" />
#       <option name="TARGET" value="" />
#       <option name="SETTINGS_FILE" value="" />
#       <option name="CUSTOM_SETTINGS" value="false" />
#       <option name="USE_OPTIONS" value="false" />
#       <option name="OPTIONS" value="" />
#       <method v="2" />
#     </configuration>
#     <configuration name="Worker" type="Python.DjangoServer" factoryName="Django server">
#       <module name="CKDemo" />
#       <option name="INTERPRETER_OPTIONS" value="" />
#       <option name="PARENT_ENVS" value="true" />
#       <envs>
#         <env name="PYTHONUNBUFFERED" value="1" />
#         <env name="DJANGO_SETTINGS_MODULE" value="pycharm" />
#       </envs>
#       <option name="SDK_HOME" value="$USER_HOME$/.virtualenvs/CKDemo/bin/python" />
#       <option name="WORKING_DIRECTORY" value="" />
#       <option name="IS_MODULE_SDK" value="false" />
#       <option name="ADD_CONTENT_ROOTS" value="true" />
#       <option name="ADD_SOURCE_ROOTS" value="true" />
#       <option name="launchJavascriptDebuger" value="false" />
#       <option name="host" value="" />
#       <option name="additionalOptions" value="-Q celery" />
#       <option name="browserUrl" value="" />
#       <option name="runTestServer" value="false" />
#       <option name="runNoReload" value="false" />
#       <option name="useCustomRunCommand" value="true" />
#       <option name="customRunCommand" value="worker" />
#       <method v="2" />
#     </configuration>
#     <configuration name="runserver" type="Python.DjangoServer" factoryName="Django server">
#       <module name="CKDemo" />
#       <option name="INTERPRETER_OPTIONS" value="" />
#       <option name="PARENT_ENVS" value="true" />
#       <envs>
#         <env name="PYTHONUNBUFFERED" value="1" />
#         <env name="DJANGO_SETTINGS_MODULE" value="pycharm" />
#       </envs>
#       <option name="SDK_HOME" value="$USER_HOME$/.virtualenvs/CKDemo/bin/python" />
#       <option name="WORKING_DIRECTORY" value="" />
#       <option name="IS_MODULE_SDK" value="false" />
#       <option name="ADD_CONTENT_ROOTS" value="true" />
#       <option name="ADD_SOURCE_ROOTS" value="true" />
#       <option name="launchJavascriptDebuger" value="false" />
#       <option name="host" value="" />
#       <option name="additionalOptions" value="" />
#       <option name="browserUrl" value="" />
#       <option name="runTestServer" value="false" />
#       <option name="runNoReload" value="false" />
#       <option name="useCustomRunCommand" value="false" />
#       <option name="customRunCommand" value="" />
#       <method v="2" />
#     </configuration>
#     <configuration name="build-prod" type="js.build_tools.npm" nameIsGenerated="true">
#       <package-json value="$PROJECT_DIR$/npm/package.json" />
#       <command value="run" />
#       <scripts>
#         <script value="build-prod" />
#       </scripts>
#       <node-interpreter value="project" />
#       <envs />
#       <method v="2" />
#     </configuration>
#     <list>
#       <item itemvalue="Django Server.runserver" />
#       <item itemvalue="Django Server.Worker" />
#       <item itemvalue="Django tests.Tests" />
#       <item itemvalue="npm.build-prod" />
#     </list>
#   </component>
