_Certificate Authority__

__certtool__ is used to parse and generate X.509 certificates, requests and private keys.

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
- To create a certificate request (needed when the certificate is issued by another party), run:
```
certtool --generate-request --load-privkey ca-key.pem --outfile request.pem
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


 - To generate a certificate using the private key only, use the command:

```
certtool --generate-certificate --load-privkey key.pem --outfile cert.pem --load-ca-certificate ca-cert.pem --load-ca-privkey ca-key.pem
```

Certificate information ( Validity / Issuer / Key Algorithm / Extensions / Signature Algorithm )
```
certtool --certificate-info --infile cert.pem
```
