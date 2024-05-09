# Installs and configures Nginx web server.

$doc_root = '/var/www/html'
$server_block = '/etc/nginx/sites-available'

package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
  before   => Exec['allow nginx']
}

service {'nginx':
  ensure => 'running',
  enable => 'true'
}

exec {'apt-get update':
  command => '/usr/bin/apt-get update -y',
  before  => Package['nginx']
}

service { 'ufw':
  ensure => 'running',
  enable => 'true'
}

exec {'allow nginx':
  command => '/usr/bin/sudo ufw allow "Nginx HTTP"',
  require => Service['ufw']
}

file {'index.html':
  ensure  => 'present',
  path    => "${doc_root}/index.html",
  content => "Hello World!\n",
  notify  => Service['nginx'],
  require => Package['nginx']
}

file {'custom_404':
  ensure  => 'present',
  path    => "${doc_root}/custom_404",
  content => "Ceci n\'est pas une page\n",
  notify  => Service['nginx'],
  require => Package['nginx']
}

file {'default':
  ensure  => 'present',
  path    => "${server_block}/default",
  backup  => 'true',
  require => Package['nginx']
}

exec {'sed':
  command => '/usr/bin/sed -i "s%server_name _;%server_name _;\n\trewrite ^/redirect_me https://pinterest.com permanent;\n\terror_page 404 /custom_404;\n\tlocation = /custom_404 {\n\t\troot /var/www/html;\n\t\tinternal;\n\t}%" /etc/nginx/sites-available/default',
  require => File['default'],
  notify  => Service['nginx']
}
