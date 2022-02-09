#!/bin/bash
heroku logs -a zachspar-dot-com -n 1500 > app-logs-$(date '+%s').log

