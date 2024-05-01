# Copyright 2022 Seth Michael Larson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import sys


def main():
    path = sys.argv[1]
    with open(path, "r") as f:
        data = f.read()

    len_before = len(data)
    data = (
        data
        # Use the system's monospace font
        .replace("font-family: Courier New", "font-family: monospace")
        .replace('font-family="Courier New"', 'font-family="monospace"')
        .replace("Courier New", "monospace")
        # Don't replace the cursor with a pointer, makes it hard to highlight text
        .replace("cursor:pointer;", "")
    )

    # Remove embedded draw.io content
    data = re.sub(r" content=\"&lt;mxfile[^\"]+?\"", "", data)
    data = re.sub(r" onclick=\"[^\"]+?\"", "", data)

    # Replace runs of 6 characters in colors with runs of 3.
    for hexchar in "0123456abcdefABCDEF":
        data = data.replace(f"#{hexchar * 6}", f"#{hexchar * 3}")

    len_after = len(data)

    if len_before != len_after:
        print(f"File size changed from {len_before} -> {len_after}")

    with open(path, "w") as f:
        f.truncate()
        f.write(data)


main()
