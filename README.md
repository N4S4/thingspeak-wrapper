# Thingspeak Wrapper

Guys I would like to share with you my wrapper,
I find it useful for my project as saves lot of lines of code
when i need to get and send data to [Thingspeak](thingspeak.com).

I would like to specify that **I am Not** a programmer as I do it all
for hobby and in my **little** free time.

## Premise

I've tried this wrapper only with python3 
I do not know if it actually runs with previous versions 
but I will test and update as soon as possible (as soon I have time).

## Prerequisites

Prior to install this wrapper you will need to install pandas dataframe library.

## Installation

Just go to repository folder and run the setup.py it wil install the wrapper for you.
from the command line go to the downloaded folder and run:

```
python3.6 setup.py install
```

## Testing

In the test folder of this repository you'll find a test.py file which initiate and run all the functions
on one of my public channels on [Thingspeak](https://thingspeak.com/channels/501309).

The test file is also commented with explanations.

## Basic Usage

```
import thingspeak_wrapper as tsw 

# Initiate the class ThingWrapper with (CHANNEL_ID, WRITE_API__KEY, READ_API_KEY)
# if is a public channel just pass the CHANNEL_ID api_key defaults are None
my_channel = tsw.wrapper.ThingWrapper(channel_id, 'write_api_key', 'read_api_key')

# send values to a field with sender(field, value)

mychannel.sender(1, 24)
```

## Available Functions

It is a very small script for now do I did not write any documentation.
I am planning  to introduce some more functions so as soon it will get mor complex I'll write it.

For now ill write them here.

the entire set of available functions are:

```
# one field and one value
my_channel.sender(field, value) 

# more fields more values; pass them as lists
my_channel.multiple_sender([fields], [values]) 

# if arguments are left empty all fields and all values are returned with a max of 8000 values
my_channel.get_json_feeds(fields='feeds', results_quantity=None) 

# you can request from and to specific dates
# dates and times must be as string type with this format 'YYYY-MM-DD' 'HH:NN:SS'
# see test.py for better instructions
my_channel.get_json_feeds_from(start_date, start_time, stop_date, stop_time, fields='feeds')

my_channel.get_xml_feeds(fields='feeds', results_quantity=None)

my_channel.get_xml_feeds_from(start_date, start_time, stop_date, stop_time, fields='feeds')

# csv data can be returned as pandas data frame and not
# just specify pandas_format=False if you don't want it as data frame
# default is True
my_channel.get_csv_feeds(fields='feeds', pandas_format=True, results_quantity=None)

my_channel.get_csv_feeds_from(start_date, start_time, stop_date, stop_time, fields='feeds')
```

## Conclusions

###### I know I know
 
is not the best snippet you ever seen but it is helping me a lot!
I hope whom is interested will contribute to improve this wrapper for a better use,
let me know if you need something!

## Contributing

Please fork it!

## Authors

- Renato Visaggio - _Initial_ _Work_ - [N4S4](https://github.com/N4S4)




# thingspeak-wrapper
