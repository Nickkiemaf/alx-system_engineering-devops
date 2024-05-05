#!/usr/bin/env bash
#using puppet to make changes to our ssh configuration file

file { 'etc/ssh/ssh-config':
       ensure => present,

content => "

        Host*
        IdentifyFile ~/.ssh/school
        PasswordAuthentication no
}
