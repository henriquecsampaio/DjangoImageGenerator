# DjangoImageGenerator

This Django web application integrates XKCD comics, random dog images and QR code generaror. 

## Features

1. **XKCD Comic Viewer:**
   - Access random XKCD comics through the `get_xkcd` URL.
   - A dedicated view renders a random XKCD comic using the [XKCD JSON API](https://xkcd.com/json.html).

2. **XKCD Comic Selection:**
   - Utilize a template with a form to allow users to enter a specific XKCD comic ID.
   - On form submission, the user is redirected to a page with the updated URL for the specified comic.

3. **Dog Image Viewer:**
   - Explore random dog images via the `get_dog` URL.
   - The `get_dog` view fetches a random dog image from the [Dog API](https://dog.ceo/api/breeds/image/random).

4. **Dog Image Customization:**
   - A template with a form enables users to input a dog breed and sub-breed.
   - The form fetches and renders images based on the user's selected breed and sub-breed.

5. **QR Code Generator:**
   - Generate QR codes through the `generate_qr_code` URL.
   - The `generate_qr_code` view renders a QR code using the [Image-Charts API](https://documentation.image-charts.com/qr-codes/).

6. **QR Code Customization:**
   - A Jinja template includes a form for users to input QR code height, width, and value.
   - The form generates and renders a QR code based on the specified parameters.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Django Development Server:**
   ```bash
   python manage.py runserver
   ```

4. **Access the Application:**
   - Open your browser and go to [http://localhost:8000/](http://localhost:8000/).

5. **Explore the Features:**
   - Navigate to the provided URLs (`get_xkcd`, `get_dog`, `generate_qr_code`) to experience the different functionalities.

