import zlib
import random
import base64
import xmlrpclib


class OpenSubtitle:

    url = "http://api.opensubtitles.org/xml-rpc"
    video = {'hash': '', 'imdbid': '', 'name': '', 'year': '', 'season': '',
             'episode': '', 'size': '', 'hashSub': '', 'nameData': ''}
    subHash = []
    language = {'English': 0,'Hindi':0}

    def __init__(self, videoHash, size, name):
        self.video['hash'] = videoHash
        self.video['nameData'] = name
        self.video['size'] = size

    def Login(self):
        server = xmlrpclib.Server(self.url)
        res = server.LogIn("", "", "en", "MyAPP V2")
        self.token = str(res['token'])
        return res

    def CheckMovieHash(self):
        server = xmlrpclib.Server(self.url)
        res = server.CheckMovieHash(self.token, [self.video['hash']])

        if len(res['data'][self.video['hash']]) != 0:
            self.video['imdbid'] = str(
                res['data'][self.video['hash']]['MovieImdbID'])
            self.video['name'] = str(
                res['data'][self.video['hash']]['MovieName'])
            self.video['year'] = str(
                res['data'][self.video['hash']]['MovieYear'])
            self.video['season'] = str(
                res['data'][self.video['hash']]['SeriesSeason'])
            self.video['episode'] = str(
                res['data'][self.video['hash']]['SeriesEpisode'])

        else:
            res = 'Error'

        return res

   

    def SearchSubtitles(self, order):
            server = xmlrpclib.Server(self.url)
            content = []
            if(order == 1):
                content.append({'moviehash': self.video['hash'],
                                'moviebytesize': self.video['size']})
            elif(order == 2):
                content.append({'imdbid': self.video['imdbid']})

            elif(order == 3):
                content.append({'name': self.video['name']})
            elif(order == 4):
                content.append({'query': self.video['name'],
                                'season': self.video['season'],
                                'episode': self.video['episode']})
            else:
                content.append({'query': self.video['nameData']})

            resp= server.SearchSubtitles(self.token, content)

            try:
                for i in range(0, len(resp['data'])):
                    self.subHash.append(
                        {'id': resp['data'][i]['IDSubtitleFile'], 'hashSub': resp['data'][i]['SubHash'], 'lang': resp['data'][i]['LanguageName']})
            except:
                resp= 'Error'
            return (resp)

    def chechDLSubtitle(self, lang, type):
        if type == 0:
            if self.language[lang] == 0:
                return False
            else:
                return True
        elif type == 1:
            resp= True

            for lang in self.language.values():
                if lang == 0:
                    resp= False
                    break
            return (resp)
        else:
            return "Error"

    def DownloadSubtitles(self):
        resp= ""
        server= xmlrpclib.Server(self.url)

        for j in self.language:
            if self.chechDLSubtitle(j, 0) == False:

                for i in range(0, len(self.subHash)):
                    if self.subHash[i]['lang'] == j:

                        self.language[j]= 1

                        resp= server.DownloadSubtitles(
                            self.token, [self.subHash[i]['id']])
                        resp= base64.standard_b64decode(
                            resp['data'][0]['data'])
                        resp= zlib.decompress(resp, 47)

                        name= self.video['name']
                        sub_file = (name + '_' + j[0: 2]).upper() + '.srt'

                        f= open(sub_file, 'wb')
                        f.write(resp)
                        f.close()
                           
                        break
        return ()

    def Logout(self):
        server= xmlrpclib.Server(self.url)
        server.LogOut(self.token)
        print("Done")
