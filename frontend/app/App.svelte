<script>
  import { Router, Route } from "svelte-routing";
  import Index from "./pages/Index.svelte";
  import VerifyUser from "./pages/VerifyUser.svelte";
  import UserProfile from './pages/UserProfile.svelte';
  import Help from "./pages/Help.svelte";
  import Datasets from "./pages/Datasets.svelte";
</script>

<Router>
  <Route path="/help" component={Help} />
  <Route path="/user" component={UserProfile} />
  <Route path="/data" component={Datasets} />
  <Route path="/verify" component={VerifyUser} />        
  <Route path="*" component={Index} />
</Router>


