# ----------------------------------------------------
# SPDX-FileCopyrightText: AsFigo Technologies, UK
# SPDX-FileCopyrightText: VerifWorks, India
# SPDX-License-Identifier: MIT
# Author: Himank Gangwal, April 04, 2025
# ----------------------------------------------------
from af_lint_rule import AsFigoLintRule
import logging

class PackageCheckRule(AsFigoLintRule):
    """Detects if a class is in the scope of a package or not"""

    def apply(self, filePath: str, data: AsFigoLintRule.VeribleSyntax.SyntaxData):
        for classNode in data.tree.iter_find_all(filter_={"tag": "kClassDeclaration"}, iter_=AsFigoLintRule.VeribleSyntax.PostOrderTreeIterator):
            className = self.getClassName(classNode)
            # print(f"C:{className}:{classNode.depth}")
            if(classNode.depth > 1):
                # print(f"class {className} may have package")
                continue
            else:
                # print(f"class {className} is missing a package")
                message = f"Found a class without a package:\n {classNode.text} \n in file: {filePath}"
                self.linter.logViolation("R115",message)


