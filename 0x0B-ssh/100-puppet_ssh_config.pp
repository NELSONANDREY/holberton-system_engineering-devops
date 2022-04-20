# PPFile that config ssh_config file.
include stdlib

file_line { 'Client configuration file':
  path =>  '/etc/ssh/ssh_config',
  line =>  'PasswordAuthentication no',
}

file_line {  'modo sad':
  path =>  '/etc/ssh/ssh_config',
  line =>  'IdentityFile ~/.ssh/school',
}
