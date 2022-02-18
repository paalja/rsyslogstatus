_Certificate Authority__

initialize directory

```
mkdir /etc/rsyslogTLS
cd /etc/rsyslogTLS

apt install -y gnutls-bin
```

Create / Generating the private key of CA

```
#       To create a DSA or elliptic curves (ECDSA) private key use the above command combined with 'dsa' or 'ecc' options.

certtool --generate-privkey --outfile ca-key.pem
certtool --generate-privkey --outfile ca-key.pem --rsa

# only root to read the CA private key
chmod 400 ca-key.pem
```

Generating certificate requests
- To create a certificate request (needed when the certificate is  issued  by another party), run:
```

certtool --generate-request --load-privkey key.pem    --outfile request.pem

If the private key is stored in a smart card you can generate a request by specifying the private key object URL.
certtool --generate-request --load-privkey "pkcs11:..."   --load-pubkey "pkcs11:..." --outfile request.pem
```
Generate the self signed public key
```
certtool --generate-self-signed --load-privkey ca-key.pem --outfile ca-cert.pem
certtool --generate-self-signed --load-privkey ca-key.pem --outfile ca-cert.pem --template=template
```

Generating a certificate
 - To generate a certificate using the previous request, use the command:

```
certtool --generate-certificate --load-request request.pem --outfile cert.pem --load-ca-certificate ca-cert.pem --load-ca-privkey ca-key.pem

```


