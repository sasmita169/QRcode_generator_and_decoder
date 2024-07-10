# QRcode_generator_and_decoder
🔒 *Admin & Buyer Login*: This  system boasts a secure login system, differentiating between administrators and buyers, providing access to product management and authentication features.and its irreversible 

📦 *Product Authentication*: Admins can effortlessly add product details such as brand, ID, date of manufacture, batch number, and product type. This information converted into a single string then hashed and encrypted, resulting in a unique QR code that sets us apart from other systems.

🔐 *Enhanced Security*: It's take security seriously! Our unique filter adds extra layer of complexity to the QR code, making it nearly impossible for attackers to replicate.

🌐 *Blockchain Integration*: I have harnessed the power of blockchain technology to ensure the utmost transparency and security in the product authentication process. All data flows are meticulously handled through a blockchain model.

🔍 *Instant Verification*: When buyers scan the QR code, this system quickly analyzes the data. If the product is genuine, it instantly displays all the product details. If it's a fake product, then  system will notify the buyer, offering peace of mind with every purchase.

@ Here First all the products details are combine into a single string
 its level one of security!
    # Combine all details into a single string
    brand = int_features1[0]
    product_id = int_features1[1]
    date_of_manufacture = int_features1[2]
    batch = int_features1[3]
    price = int_features1[4]
    product_type = int_features1[5]

    product_details = f"{brand}{product_id}{date_of_manufacture}{batch}{price}{product_type}"
@ After that string will be converted into hash code
 Generate a hash code using SHA-256 
    hash_code = hashlib.sha256(product_details.encode()).hexdigest()

    #print(hashed_password)

    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import serialization, hashes
    import binascii

    # Load keys from files
    hashed_password=hash_code
    loaded_private_key, loaded_public_key = load_keys()
    #message =hashed_password
    message =hashed_password.encode()  # Convert string to bytes
@Encrypted then Decrypted

    # Encrypt using loaded public key
    ciphertext = loaded_public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Decrypt using loaded private key
    plaintext = loaded_private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
Key Functions and Modules Used
cryptography.hazmat: This module provides low-level cryptographic primitives.
hashlib: Used for hashing data using SHA-512.
binascii: Handles binary-to-text (hexadecimal) and text-to-binary conversions.
block2.protect_data2: Presumably a custom function or module for further data protection.
Key Operations in Your Script
Loading RSA Keys:

Keys are loaded from private_key.pem and public_key.pem using serialization.load_pem_private_key and serialization.load_pem_public_key.
Hashing Data:

Data (in this case, hashcode_data) is hashed using SHA-512 to generate a hexadecimal representation (hashed_password).
Encrypting Data:

The hashed data (message) is encrypted using RSA encryption with OAEP padding (padding.OAEP) and the loaded public key (loaded_public_key.encrypt).
Decrypting Data:

Encrypted data (ciphertext) is decrypted using the private key (loaded_private_key.decrypt).
Further Data Protection:

After encryption, the ciphertext is passed to protect_data2 (presumably another layer of protection or processing).

step:1 
Click on manufacturer 

![Screenshot 2024-07-10 094146](https://github.com/sasmita169/QRcode_generator_and_decoder/assets/118671759/a95d1734-f5c8-43c4-93b9-26954f513d2f)
step: 2 
Admin needs to login

![Screenshot 2024-07-10 094212](https://github.com/sasmita169/QRcode_generator_and_decoder/assets/118671759/c854211c-3f7d-4698-aa34-828bec832413)
step:3 
Then all product details

![Screenshot 2024-07-10 094319](https://github.com/sasmita169/QRcode_generator_and_decoder/assets/118671759/01361693-08c7-4c72-8e6d-f83c3e048291)
step: 4 
Then system create a QRcode

![Screenshot 2024-07-10 094305](https://github.com/sasmita169/QRcode_generator_and_decoder/assets/118671759/160fd2f8-5e91-4ce8-8a18-b99b08422ebe)
step :5 
Then Goto Buyer start camera if its genuine product then its show product details other wise shows fake product !

![Screenshot 2024-07-10 094823](https://github.com/sasmita169/QRcode_generator_and_decoder/assets/118671759/885c9189-0bc4-4fd2-920f-05be108a7e08)

![Screenshot 2024-07-10 095305](https://github.com/sasmita169/QRcode_generator_and_decoder/assets/118671759/46c7f0cf-1650-433b-bc9d-ba1d4e430e7f)

![Screenshot 2024-07-10 095358](https://github.com/sasmita169/QRcode_generator_and_decoder/assets/118671759/4ee0b370-9994-461d-b9a0-e8209bbd49ed)

