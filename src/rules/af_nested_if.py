# ----------------------------------------------------
# SPDX-FileCopyrightText: AsFigo Technologies, UK
# SPDX-FileCopyrightText: VerifWorks, India
# SPDX-License-Identifier: MIT
# Author: Himank Gangwal April 27, 2025
# ----------------------------------------------------
from af_lint_rule import AsFigoLintRule
import logging

class NoNestedIfRule(AsFigoLintRule):
    """Detects if there are 4 or more nested if loops."""

    def apply(self, filePath: str, data: AsFigoLintRule.VeribleSyntax.SyntaxData):
        # an array storing depth values and the index indicates the level of nesting
        # in anytree the depth values are monotonically increasing with nesting
        # level = 0
        depthStore = [0]
        for classNode in data.tree.iter_find_all({"tag": "kClassDeclaration"}):
            className = self.getClassName(classNode)
            # max_value = 0
            # filter both case and if using ConditionalStatement and CaseStatement
            # change the order of iteration to be preOdrder to walk to code line by line
            for varNode in classNode.iter_find_all(filter_={"tag": ["kConditionalStatement", "kCaseStatement"]}, iter_=AsFigoLintRule.VeribleSyntax.PreOrderTreeIterator):
                level = varNode.depth // 5
                   
                if (level >= 4):
                    message = f"Found 4 or more nested if loops: {varNode.text} in file: {filePath}"
                    self.linter.logViolation("R120",message)

        
              
