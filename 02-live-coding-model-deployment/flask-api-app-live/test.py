from channel import Channel, ChannelList


channel_list = ChannelList()


channel_list.load_json("channels.json")


for channel  in channel_list.get_all():

    print(channel.to_dict())