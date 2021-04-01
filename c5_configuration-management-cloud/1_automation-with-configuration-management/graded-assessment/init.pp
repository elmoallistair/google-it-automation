class profile {
        file { '/etc/profile.d/append-path.sh':
                owner   => 'root',
                group   => 'root',
                mode    => '0644',
                content => "PATH=\$PATH:/java/bin\n",
        }
}