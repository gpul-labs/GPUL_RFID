import time

from src.dao.loggerdao import LoggerDAO


class HTTPServerDatasource(object):
    def __init__(self):

        self.running = True
        self.logger_dao = LoggerDAO()
        self.doc_root_file = '/srv/rfid_logger_http/index.html'

    def run(self):

        while self.running:
            time.sleep(2)
            entries = self.logger_dao.get_entries()
            html = '<table width="500px" border="1"><thead><th width="20%">id</th><th width="40%">event</th><th width="40%">moment</th></thead><tbody>'

            for r in entries:
                html += '<tr><td width="20%">' + str(r['id']) + '</td><td width="40%">' + r[
                    'event'] + '</td><td width="40%">' + str(r['moment']) + '</td></tr>'
            html += '</tbody></table><script>setTimeout(function(){window.location.reload(1);}, 2000)</script>'

            with open(self.doc_root_file, 'w') as f:
                f.write(html)


if __name__ == '__main__':
    ds = HTTPServerDatasource()
    ds.run()
