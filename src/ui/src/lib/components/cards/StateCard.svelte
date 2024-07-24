<script>
    import { Badge, Card, Alert } from 'flowbite-svelte';
	import { InfoCircleSolid } from 'flowbite-svelte-icons';
	export let states = [
		{
			stateOption: '',
		}
	]
</script>

<div class="bg-white py-24 sm:py-8">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl lg:mx-0">
        <span><h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">State</h2></span>
        <div class="section status">
            <Card class="m-4 " color="primary">Delay: [Reason]</Card>
        </div>

      </div>
      <div class="mx-auto mt-10 grid max-w-2xl grid-cols-1 gap-x-0 gap-y-16 border-t border-gray-200 pt-10 sm:mt-8 sm:pt-8 lg:mx-0 lg:max-w-2xl lg:grid-cols-3">
        {#each states as state}
        <div class="flex max-w-44 flex-col p-2 items-start justify-between rounded-[10px] border-2 border-black">
          <div class="flex items-center gap-x-4 text-xs">
            <time datetime="2020-03-16" class="text-gray-500">Mar 16, 2020</time>
          </div>
          <div class="group relative">
            <p class="mt-5 line-clamp-3 text-xl leading-6 text-gray-600">{state.stateOption}</p>
          </div>
          </div>
          {/each}
      </div>

    </div>

  </div>