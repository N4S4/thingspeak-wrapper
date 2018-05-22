import time

import thingspeak_wrapper as tsw

# Initiate the class ThingWrapper with (CHANNEL_ID, WRITE_API__KEY, READ_API_KEY)
# if is a public channel just pass the CHANNEL_ID argument, api_key defaults are None
my_channel = tsw.wrapper.ThingWrapper(501309, '6TQDNWJQ44FA0GAQ', '10EVD2N6YIHI5O7Z')


# all set of functions are:
# my_channel.sender()
# my_channel.multiple_sender()
# my_channel.get_json_feeds()
# my_channel.get_json_feeds_from()
# my_channel.get_xml_feeds()
# my_channel.get_xml_feeds_from()
# my_channel.get_csv_feeds()
# my_channel.get_csv_feeds_from()

# ---------------------------
# Now you can use all the possible functions
# Send a value to a single field
my_channel.sender(1, 4)

# this delay is due to limitation of thingspeak free account which allow you to post data every 15 sec minimum
time.sleep(15)

# ---------------------------
# Send data to multiple field
# It take 2 input as lists ([..], [..])
# Create lists of fields and values
fields = [1, 2, 3]
values = [22.0, 1029, 700]
# pass them to the function
my_channel.multiple_sender(fields, values)

# ---------------------------
# Get data functions returns data as json, xml, csv
# optionally csv can be returned as Pandas Data frame
# pass arguments to the function (field, data_quantity)
# default values are ( fields='feeds', results_quantity=None)
# you will get all fields and all values (max 8000)
json_field1 = my_channel.get_json_feeds(1, 300)
print(json_field1)

# get xml data pass same values as previous function
xml_field1 = my_channel.get_xml_feeds(1, 300)
print(xml_field1)

# get csv data
# this function requires to specify (field, pandas_format=True, result_quantity=None)
# defaults are (fields='feeds', pandas_format=True, result_quantity=None)
csv_field1 = my_channel.get_csv_feeds(1, pandas_format=True,
                                      results_quantity=300)
print(csv_field1)

# data without pandas_format
csv_no_pandas = my_channel.get_csv_feeds(1, pandas_format=False,
                                         results_quantity=300)
print(csv_no_pandas)

# there is the possibility to request data from and to specific dates
# set date and time as strings YYYY-MM-DD HH:NN:SS
start_date, start_time = '2018-05-21', '12:00:00'
stop_date, stop_time = '2018-05-21', '23:59:59'

# pass values to the function
# defaults are (start_date, start_time, stop_date=None, stop_time=None, fields='feeds')
values_from_date = my_channel.get_json_feeds_from(stop_date, start_time, stop_date, stop_time, 1)

print(values_from_date)
