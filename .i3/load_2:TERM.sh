#!/bin/bash
i3-msg "workspace 2:TERM; append_layout ~/.i3/workspace_2:TERM.json"

(~/.bin/start-htop &)
(~/.bin/start-ncmpcpp &)
(urxvt &)
