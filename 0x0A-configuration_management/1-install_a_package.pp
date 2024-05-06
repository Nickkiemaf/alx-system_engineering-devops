#!/usr/bin/puppet

# Puppet manifest to install Flask version 2.1.0 and Werkzeug version 2.1.1 using pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => Package['python3-pip'],
}

package { 'python3-pip':
  ensure => installed,
}
