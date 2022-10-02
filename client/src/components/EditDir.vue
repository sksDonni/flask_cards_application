<template>
    <div>
        <h1> Edit Directory </h1>
        <hr />
        <button @click="populate">populate</button>
        <form @submit.prevent @submit="edit_deck">
            <div>
                <label>Name</label>
                <input type="text" v-model="values.dir_name" />
            </div>
            <button type="submit" class="main-button">Submit</button>
        </form>
    </div>
</template>

<script>
import { mapState } from 'vuex'
export default{
    data(){
        return{
            values:{
                dir_name:'',
            },
        }
    },
    methods:{
        edit_deck(){
            let dir_id = this.dir_id
            let data_submitted = { ...this.values, dir_id}
            console.log(data_submitted)
            this.$store.dispatch("editDirById", data_submitted)
            .then(res => {
                if(res.status == 200){
                    this.$router.push(`/`)
                }
            })
        },
        populate(){
            this.values.dir_name = this.dir_name
        }
    },
    computed:{
        ...mapState({
            dir_id: state => state.individualDir.dir_id,
            dir_name: state => state.individualDir.dir_name
        }),
    },
    mounted(){
        let id = this.$route.params.id
        this.$store.dispatch("fetchDirectoryById", {id})
    }
}
</script>
