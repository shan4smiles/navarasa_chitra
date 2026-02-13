# Navarasa Chitra: An Interactive Emotional Mandala

**Navarasa Chitra** is a living, breathing work of art — a collective mandala that grows and evolves based on the emotional contributions of a group. This project blends ancient Indian aesthetics (Navarasas), traditional color theories (Sapta Varna), and elemental philosophy (Pancha Bhuta) with modern interactive technology.

## Project Structure

- `app.py`: The Flask backend that manages the state of the session.
- `templates/index.html`: The **Participant Interface**. A mobile-friendly web app where users select an emotion, blend their custom color, and choose a texture.
- `templates/mandala.html`: The **Global Display**. A visual centerpiece meant to be projected on a large screen, showing the concentric rings of the group's collective "Emotional Footprint".
- `data/mandala_state.json`: Permenant record of all submissions.

## Core Concepts

### 1. Navarasa (The 9 Emotions)
The mandala is divided into 9 angular sectors, each representing a core Rasa:
- **Shringara** (Love), **Hasya** (Joy), **Karuna** (Compassion), **Raudra** (Anger), **Veera** (Heroism), **Bhayanaka** (Fear), **Bibhatsa** (Disgust), **Adbhuta** (Wonder), **Shanta** (Peace).

### 2. Sapta Varna (The 7 Colors)
Participants create their own "Emotional Hue" using 7 sliders representing traditional colors (Red, Orange, Yellow, Green, Blue, Indigo, White). These blend in real-time to create a harmonious custom color.

### 3. Pancha Bhuta (The 5 Elements)
To add depth, each participant chooses an elemental texture that overlays their color:
- **Earth (Prithvi)**: Solid Grid Patterns.
- **Water (Apas)**: Flowing Curves.
- **Fire (Agni)**: Sharp Zigzags.
- **Air (Vayu)**: Spirals & Swirls.
- **Space (Akasha)**: Vibrant Dots.

## How to Run

1.  Navigate to the project directory:
    ```bash
    cd "Navarasa Chitra"
    ```
2.  Start the Flask server:
    ```bash
    python app.py
    ```
3.  **For Participants**: Open `http://localhost:5000` on any device.
4.  **For the Main Screen**: Open `http://localhost:5000/mandala_display` on a projector or large monitor.

## Experience
Every submission adds a new concentric ring to the mandala. Only the sector corresponding to the participant's chosen emotion is filled. As more people participate, the mandala blooms outward, creating a vibrant, intricate tapestry of the group's evolving collective mood.
