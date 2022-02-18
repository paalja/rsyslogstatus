--CA--

```
mkdir /etc/rsyslogTLS
cd /etc/rsyslogTLS

apt install -y gnutls-bin

# create the private key of CA
certtool --generate-privkey --outfile ca-key.pem
chmod 400 ca-key.pem

# generate the self signed public key
certtool --generate-self-signed --load-privkey ca-key.pem --outfile ca.pem
certtool --generate-self-signed --load-privkey ca-key.pem --outfile ca.pem --template=template

```

