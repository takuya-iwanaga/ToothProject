<template>
    <Header title="Medical Box"/>
<div> <font size="+2">{{ $store.state.userinfo.user_name }}</font>様のMedical Box</div>

<div>医院からのメッセージはありません</div>
</template>
<script setup>
import Header from '../Header.vue';

</script>