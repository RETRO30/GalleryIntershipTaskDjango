<template>
  <div class="flex flex-col min-h-screen bg-gray-900 text-white">
    <div class="sticky top-0 z-10 bg-gray-800 shadow-md p-4">
      <div class="flex flex-wrap gap-2">
        <input type="file" accept="image/*" @change="handleFile"
          class="bg-gray-700 text-white p-2 rounded border border-gray-600" />
        <input v-model="description" placeholder="Описание"
          class="bg-gray-700 text-white p-2 rounded border border-gray-600" />
        <button @click="uploadImage" :disabled="!imageBase64"
          class="bg-blue-500 hover:bg-blue-600 disabled:bg-gray-600 text-white px-4 py-2 rounded">
          Отправить
        </button>
      </div>
    </div>

    <div class="p-4 flex flex-wrap gap-4 justify-center overflow-y-auto">
      <div v-for="img in images" :key="img.id"
        class="w-48 bg-gray-800 rounded-lg shadow-lg p-3 flex flex-col items-center">
        <img :src="img.image_base64" class="rounded w-full mb-2" />
        <p class="text-sm text-center mb-2">{{ img.description }}</p>
        <button @click="deleteImage(img.id)" class="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded">
          Удалить
        </button>
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
  if (!file) return
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
