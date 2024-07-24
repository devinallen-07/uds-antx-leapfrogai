<script>
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
    import doug from '$lib/images/Unicorn-Delivery-Service.svg';
	import NavContainer from 'flowbite-svelte/NavContainer.svelte';
    import aiAntxfrom from '$lib/images/AI-ANTX.png';
  </script>

<Navbar class="bg-[#0c163d]" >
    <NavBrand>
      <img src={doug} class="me-3 h-6 sm:h-9" alt="UDS" />
    </NavBrand>
    <NavHamburger  />
    <NavUl >
        <img src={aiAntxfrom} class="me-3 h-8 lg:h-9" alt="UDS" />
    </NavUl>
  </Navbar>