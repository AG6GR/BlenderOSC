import argparse
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("-p", "--port", type=int, default=5005,
      help="The port the OSC server is listening on")
  parser.add_argument("-t", "--type", default="str", help="OSC message data type");
  parser.add_argument("path", help="OSC path")
  parser.add_argument("message", help="OSC message content")
  args = parser.parse_args()

  content = args.message;
  if args.type == "int":
      content = int(content);
  elif args.type == "float":
      content = float(content);

  client = udp_client.SimpleUDPClient(args.ip, args.port)
  client.send_message(args.path, content);