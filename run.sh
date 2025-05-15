#!/bin/bash

BOT_TOKEN="8054991584:AAF-VmW1-YPLZG_mQ3HHL9kkbAcGEdU0iAc"
USER_ID="7069636058"

while true; do
    echo "[watchdog] Starting app.py..."
    python3 /home/user/Vps/app.py

    echo "[watchdog] app.py exited. Restarting in 10 seconds..."

    curl -s -X POST https://api.telegram.org/bot$BOT_TOKEN/sendMessage \
        -d chat_id=$USER_ID \
        -d text="⚠️ تم إعادة تشغيل app.py تلقائيًا من watchdog.sh"

    sleep 10
done
