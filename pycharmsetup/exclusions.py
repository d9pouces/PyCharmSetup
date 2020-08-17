import os
import re
import xml.etree.ElementTree as ET
from typing import List

from pycharmsetup.cli import PyCharmConfig


def read_exclusions_from_pc(pc_config: PyCharmConfig) -> List[str]:
    xml_root = ET.parse(
        os.path.join(pc_config.project_dir, ".idea", "%s.iml" % pc_config.module)
    )
    exclusions = []  # type: List[str]
    for elt in xml_root.findall(
        "./"
        'module[@type="PYTHON_MODULE"][version="4"]/'
        'component[@name="NewModuleRootManager"]/'
        'content[@url="file://$MODULE_DIR$"]/'
        "excludeFolder[@url]"
    ):
        url = elt.get("url") or ""
        matcher = re.match(r"^file://\$MODULE_DIR\$/(.*)$", url)
        if matcher:
            exclusions.append(matcher.group(1))
    return exclusions

# modules.xml:      <module fileurl="file://$PROJECT_DIR$/.idea/CKDemo.iml" filepath="$PROJECT_DIR$/.idea/CKDemo.iml" />
# CKDemo.iml
# <?xml version="1.0" encoding="UTF-8"?>
# <module type="PYTHON_MODULE" version="4">
#   <component name="NewModuleRootManager">
#     <content url="file://$MODULE_DIR$">
#       <excludeFolder url="file://$MODULE_DIR$/.idea" />
#       <excludeFolder url="file://$MODULE_DIR$/.mypy_cache" />
#       <excludeFolder url="file://$MODULE_DIR$/.tox" />
#       <excludeFolder url="file://$MODULE_DIR$/build" />
#       <excludeFolder url="file://$MODULE_DIR$/df_site/static/css" />
#       <excludeFolder url="file://$MODULE_DIR$/df_site/static/js" />
#       <excludeFolder url="file://$MODULE_DIR$/metier.egg-info" />
#     </content>
#     <orderEntry type="jdk" jdkName="Pipenv (CKDemo)" jdkType="Python SDK" />
#     <orderEntry type="sourceFolder" forTests="false" />
#   </component>
