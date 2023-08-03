<template>
  <div>
    <Sidebar />
    <div class="wrapper d-flex flex-column min-vh-100 bg-light">
      <Header></Header>
      <div class="body flex-grow-1 px-3">
        <CContainer>
          <router-view />
        </CContainer>
      </div>
      <Footer></Footer>
    </div>
  </div>
</template>
<script>
import { CContainer } from "@coreui/vue";
import Sidebar from "@/components/Sidebar.vue";
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "DefaultLayout",
  components: {
    Sidebar,
    Header,
    Footer,
    CContainer,
  },
};
</script>
