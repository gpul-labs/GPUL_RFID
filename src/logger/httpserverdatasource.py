#!/usr/bin/python
import time
import sys
import threading
sys.path.append("../")
from dao.loggerdao import LoggerDAO


class HTTPServerDatasource(object):
    def __init__(self, ipc):
        self.running = ipc
        self.logger_dao = LoggerDAO()
        self.doc_root_file = '/srv/rfid_logger_http/index.html'

    def run(self):

        while self.running.is_set():
            time.sleep(2)
            entries = self.logger_dao.get_entries()
            html = '<img src="capture.jpg" width="50%" height="50%"></br><table width="500px" border="1"><thead><th width="20%">id</th><th width="40%">event</th><th width="40%">moment</th></thead><tbody>'

            for r in entries:
                html += '<tr><td width="20%">' + str(r['id']) + '</td><td width="40%">' + r[
                    'event'] + '</td><td width="40%">' + str(r['moment']) + '</td></tr>'
            html += '</tbody></table><script>setTimeout(function(){window.location.reload(1);}, 2000)</script>'

            with open(self.doc_root_file, 'w') as f:
                f.write(html)


