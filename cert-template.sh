# X.509 Certificate options
#
# DN options

# The organization of the subject.
organization = "Equinor"

# The organizational unit of the subject.
unit = "Equinor Cyber Defense Center Detect"

# The locality of the subject.
locality = Stavanger

# The state of the certificate owner.
state = "Rogaland"

# The country of the subject. Two letter code.
country = NO

# The common name of the certificate owner. / Common Name (CN) / FQDN / .example.com / www.example.com
cn = "k8-ca"

# A user id of the certificate owner.
uid = "PJA"

# If the supported DN OIDs are not adequate you can set
# any OID here.
# For example set the X.520 Title and the X.520 Pseudonym
# by using OID and string pairs.
#dn_oid = "2.5.4.12" "Dr." "2.5.4.65" "jackal"

# This is deprecated and should not be used in new
# certificates.
# pkcs9_email = "none@none.org"

# The serial number of the certificate
serial = 20220218

# In how many days, counting from today, this certificate will expire.
expiration_days = 365

# X.509 v3 extensions

# A dnsname in case of a WWW server.
#dns_name = "www.none.org"
#dns_name = "www.morethanone.org"

# An IP address in case of a server.
ip_address = "10.2.0.6"

# An email in case of a person
email = "pja@equinor.com"

# An URL that has CRLs (certificate revocation lists)
# available. Needed in CA certificates.
#crl_dist_points = "http://www.getcrl.crl/getcrl/"

# Whether this is a CA certificate or not
ca

# Whether this certificate will be used for a TLS client
tls_www_client

# Whether this certificate will be used for a TLS server
tls_www_server

# Whether this certificate will be used to sign data (needed
# in TLS DHE ciphersuites).
signing_key

# Whether this certificate will be used to encrypt data (needed
# in TLS RSA ciphersuites). Note that it is preferred to use different
# keys for encryption and signing.
encryption_key

# Whether this key will be used to sign other certificates.
cert_signing_key

# Whether this key will be used to sign CRLs.
crl_signing_key

# Whether this key will be used to sign code.
#code_signing_key

# Whether this key will be used to sign OCSP data.
ocsp_signing_key
