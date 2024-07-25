<script>
	import Navbar from '$lib/components/Header/Navbar.svelte';
	import '../app.css';
	import { DarkMode } from 'flowbite-svelte';
</script>

<Navbar />
<slot>
	<DarkMode />
</slot>
