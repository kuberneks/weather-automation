#!/bin/bash

echo "===== 🖥️ System Info Report ====="
echo "📅 Date: $(date)"
echo "⏱️ Uptime: $(uptime -p)"
echo "👤 User: $USER"
echo ""
echo "🧠 Memory Usage:"
free -h
echo ""
echo "💾 Disk Usage:"
df -h | grep '^/dev'
echo ""
echo "🔥 Top 5 CPU Processes:"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -n 6
