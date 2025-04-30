<template>
  <div class="container">
    <h1>Галерея</h1>
    <input type="file" accept="image/*" @change="handleFile" />
    <input v-model="description" placeholder="Описание" />
    <button @click="uploadImage" :disabled="!imageBase64">Отправить</button>

    <div class="gallery">
      <div class="card" v-for="img in images" :key="img.id">
        <img :src="img.image_base64" alt="" />
        <p>{{ img.description }}</p>
        <button @click="deleteImage(img.id)">Удалить</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import imageCompression from 'browser-image-compression'

const API = import.meta.env.VITE_API_URL
const images = ref([])
const imageBase64 = ref('')
const description = ref('')

const fetchImages = async () => {
  const res = await fetch(`${API}/images/`)
  images.value = await res.json()
}

const handleFile = async (e) => {
  const file = e.target.files[0]
  const compressed = await imageCompression(file, { maxWidthOrHeight: 512, maxSizeMB: 1 })
  imageBase64.value = await imageCompression.getDataUrlFromFile(compressed)
}

const uploadImage = async () => {
  await fetch(`${API}/images/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ image_base64: imageBase64.value, description: description.value }),
  })
  imageBase64.value = ''
  description.value = ''
  fetchImages()
}

const deleteImage = async (id) => {
  await fetch(`${API}/images/${id}/`, { method: 'DELETE' })
  fetchImages()
}

onMounted(fetchImages)
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: auto;
  text-align: center;
}
.gallery {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 2rem;
}
.card {
  width: 200px;
  border: 1px solid #ccc;
  padding: 1rem;
}
img {
  width: 100%;
  height: auto;
}
</style>
