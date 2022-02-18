--CA--

```
mkdir /etc/rsyslogTLS
cd /etc/rsyslogTLS

apt install -y gnutls-bin

# create the private key of CA
certtool --generate-privkey --outfile ca-key.pem
certtool --generate-privkey --outfile ca-key.pem --rsa
       
#       To create a DSA or elliptic curves (ECDSA) private key use the above command combined with
#       'dsa' or 'ecc' options.


chmod 400 ca-key.pem

# generate the self signed public key
certtool --generate-self-signed --load-privkey ca-key.pem --outfile ca-cert.pem
certtool --generate-self-signed --load-privkey ca-key.pem --outfile ca-cert.pem --template=template

```

