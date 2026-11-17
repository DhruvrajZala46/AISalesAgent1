#!/bin/bash
# pipeline.sh <prefix>: download every key in picks.md, compress, then shots / duplicates / reuse / strips / AI scan
cd /tmp/claude-0/-home-user-AISalesAgent1/140e17c2-af15-50d0-a685-731162836c6b/scratchpad/cdi
python3 /home/user/AISalesAgent1/classy-academy-test/workflow/tools/dlpicks.py > dl_$1.log 2>&1
python3 shrink.py > shrink_$1.log 2>&1
bash post.sh $1
echo PIPELINEDONE $1
