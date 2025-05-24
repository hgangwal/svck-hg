# ----------------------------------------------------
# SPDX-FileCopyrightText: AsFigo Technologies, UK
# SPDX-FileCopyrightText: VerifWorks, India
# SPDX-License-Identifier: MIT
# Author: Himank Gangwal, April 27, 2025
# ----------------------------------------------------
from af_lint_rule import AsFigoLintRule
import anytree
import logging

class PackageCheckRule(AsFigoLintRule):
    """Detects if a class is in the scope of a package or not"""

    def apply(self, filePath: str, data: AsFigoLintRule.VeribleSyntax.SyntaxData):
        # we used preOrder to go code line by line
        for classNode in data.tree.iter_find_all(filter_={"tag": "kClassDeclaration"}, iter_=AsFigoLintRule.VeribleSyntax.PreOrderTreeIterator):
            className = self.getClassName(classNode)
            
            if('kPackageItemList' not in classNode.parent.tag):
                print(f"{className}:Error no package")
                message = f"Found a class without a package:\n {classNode.text} \n in file: {filePath}"
                self.linter.logViolation("R115",message)


