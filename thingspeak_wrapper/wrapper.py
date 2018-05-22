import json
from urllib import request, parse

import pandas as pd


class ThingWrapper:

    def __init__(self, channel, write_api_key=None, read_api_key=None):
        self.channel = channel
        self.read_api_key = read_api_key
        self.write_api_key = write_api_key

    def sender(self, field, value):
        data = parse.urlencode({'api_key': self.write_api_key, 'field' + str(field): str(value)}).encode()
        req = request.Request('http://api.thingspeak.com/update/',
                              data=data)
        resp = request.urlopen(req)
        return resp

    def multiple_sender(self, fields, values):
        a = ''
        for x in range(len(fields)):
            a += '&field' + str(fields[x]) + '=' + str(values[x])
        req = request.Request('http://api.thingspeak.com/update?api_key=' + self.write_api_key + a)
        resp = request.urlopen(req)
        return resp

    # print(sender('CFK2UMY7VRVD9X21', 1, 15))

    def get_json_feeds(self, fields='feeds', results_quantity=None):
        if results_quantity:
            if self.read_api_key:
                url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/fields/' + str(
                    fields) + '.json?key=' + self.read_api_key + '&results=' + str(results_quantity)
            else:
                url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/fields/' + str(
                    fields) + '.json?results=' + str(results_quantity)
            u_open = request.urlopen(url).read().decode('utf-8')
            feeds = json.loads(u_open)
            return feeds

        else:
            if self.read_api_key:
                url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/fields/' + str(
                    fields) + '.json?key=' + self.read_api_key
            else:
                url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/fields/' + str(
                    fields) + '.json'
            u_open = request.urlopen(url).read().decode('utf-8')
            feeds = json.loads(u_open)
            return feeds

    def get_xml_feeds(self, fields='feeds', results_quantity=None):
        if results_quantity:
            if self.read_api_key:
                url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/fields/' + str(
                    fields) + '.xml?key=' + self.read_api_key + \
                      '&results=' + str(results_quantity)
                xml = request.urlopen(url).read()
                return xml
            else:
                url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/fields/' + str(
                    fields) + '.xml?results=' + str(results_quantity)
                xml = request.urlopen(url).read()
                return xml
        else:
            if self.read_api_key:
                url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/fields/' + str(
                    fields) + '.xml?key=' + self.read_api_key
                xml = request.urlopen(url).read()
                return xml
            else:
                url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/fields/' + str(fields) + '.xml'
                xml = request.urlopen(url).read()
                return xml

    def get_csv_feeds(self, fields='feeds', pandas_format=True, results_quantity=None):
        if results_quantity:
            if self.read_api_key:
                if pandas_format:
                    url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/fields/' + str(
                        fields) + '.csv?key=' + self.read_api_key + \
                          '&results=' + str(results_quantity)
                    csv_feed = pd.read_csv(url)
                    return csv_feed
                else:
                    url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/fields/' + str(
                        fields) + '.csv?key=' + self.read_api_key + \
                          '&results=' + str(results_quantity)
                    csv_raw = request.urlopen(url).read()
                    return csv_raw
            else:
                if pandas_format:
                    url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/fields/' + str(
                        fields) + '.csv?results=' + str(results_quantity)
                    csv_feed = pd.read_csv(url)
                    return csv_feed
                else:
                    url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/fields/' + str(
                        fields) + '.csv?key=' + self.read_api_key + \
                          '&results=' + str(results_quantity)
                    csv_raw = request.urlopen(url).read()
                    return csv_raw
        else:
            if self.read_api_key:
                if pandas_format:
                    url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/fields/' + str(
                        fields) + '.csv?key=' + self.read_api_key
                    csv_feed = pd.read_csv(url)
                    return csv_feed
                else:
                    url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/fields/' + str(
                        fields) + '.csv?key=' + self.read_api_key
                    csv_raw = request.urlopen(url).read()
                    return csv_raw
            else:
                if pandas_format:
                    url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/fields/' + str(fields) + '.csv'
                    csv_feed = pd.read_csv(url)
                    return csv_feed
                else:
                    url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/fields/' + str(fields) + '.csv'
                    csv_raw = request.urlopen(url).read()
                    return csv_raw

    def get_json_feeds_from(self, start_date, start_time, stop_date=None, stop_time=None, fields='feeds'):
        if self.read_api_key:
            url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/' + str(
                fields) + '.json?key=' + self.read_api_key + \
                  '&start=' + start_date + '%20' + start_time + '&amp;end=' + stop_date + '%20' + stop_time
            u_open = request.urlopen(url).read().decode('utf-8')
            feeds = json.loads(u_open)
            return feeds
        else:
            url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/' + str(
                fields) + '.json?start=' + start_date + '%20' + start_time + \
                  '&amp;end=' + stop_date + '%20' + stop_time
            u_open = request.urlopen(url).read().decode('utf-8')
            feeds = json.loads(u_open)
            return feeds

    def get_xml_feeds_from(self, start_date, start_time, stop_date, stop_time, fields='feeds'):
        if self.read_api_key:
            url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/' + str(
                fields) + '.xml?key=' + self.read_api_key + \
                  '&start=' + start_date + '%20' + start_time + '&amp;end=' + stop_date + '%20' + stop_time
            u_open = request.urlopen(url).read().decode('utf-8')
            feeds = json.loads(u_open)
            return feeds
        else:
            url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/' + str(
                fields) + '.xml?start=' + start_date + '%20' + start_time + \
                  '&amp;end=' + stop_date + '%20' + stop_time
            u_open = request.urlopen(url).read().decode('utf-8')
            feeds = json.loads(u_open)
            return feeds

    def get_csv_feeds_from(self, start_date, start_time, stop_date, stop_time, fields='feeds'):
        if self.read_api_key:
            url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/' + str(
                fields) + '.csv?key=' + self.read_api_key + \
                  '&start=' + start_date + '%20' + start_time + '&amp;end=' + stop_date + '%20' + stop_time
            csv_feed = pd.read_csv(url)
            return csv_feed
        else:
            url = 'http://api.thingspeak.com/channels/' + str(self.channel) + '/' + str(
                fields) + '.csv?start=' + start_date + '%20' + start_time + \
                  '&amp;end=' + stop_date + '%20' + stop_time
            csv_feed = pd.read_csv(url)
            return csv_feed
