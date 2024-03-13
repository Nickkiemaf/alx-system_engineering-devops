#!/usr/bin/env ruby
from = ARGV[0].match(/\[from:(?<first>\+?\d{11}?\w+?)\]/)
to = ARGV[0].match(/\[to:(?<second>\+?\d{11}?\w+?)\]/)
flags = ARGV[0].match(/\[flags:(?<third>(-?[01]:?)+)\]/)
puts from[:first] + ',' + to[:second] + ',' + flags[:third]
