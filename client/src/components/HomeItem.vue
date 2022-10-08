<script setup>
  import {mapState} from "vuex"
</script>

<template>
  <div>
    <h2 class="">
      <button class="such-button main-button"><router-link :to="{name: 'add_dir'}">
        Add Directories
      </router-link></button>
    </h2>

    <div class="dir-wrapper">
      <div v-for="dir in directories" :key="dir" class="directories">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQP1PlabcOmG1AcNq7ujvrdeLzdgR9fPXNISvdhFEliZRMLC_RoQ1Afa3gn-ASuNh8TOrk&usqp=CAU">
        <router-link :to="{name: 'directory', params:{id: dir.dir_id}}"><h3>{{ dir.dir_name }}</h3></router-link>
        <button class="such-button">
          <router-link :to="{name: 'edit_dir', params:{id:dir.dir_id}}">
             Edit Directory
          </router-link>
        </button>
        <button class="such-button" @click="delete_dir(dir.dir_id)">
          Delete Directory
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // directories: this.$store.state.directories
    }
  },
  methods:{
    delete_dir(id){
      console.log(id)
      this.$store.dispatch("deleteDirById", {id})
      .then(res => {
        if(res.status == 200){
          this.$router.push(`/`)
        }
      })
    },
    get_directories(){
      console.log("called")
      this.$store.dispatch("fetchDirectories")
      .then(res => {
        if(res.status == 200){
          console.log(res)
        }
      })
      console.log(this.$store.state.directories)
    }
  },
  computed:{
    ...mapState({
      directories: state => state.directories
    })
  },
  created(){
    this.get_directories()
  }
}
</script>
