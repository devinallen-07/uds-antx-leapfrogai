<script>
	import Header3 from '$lib/components/Header3.svelte'
	import Header4 from '$lib/components/Header4.svelte'
	export let testimonials = [
		{
			title1: '',
			title2: ''
		}
	]
</script>

<div class="flex flex-wrap items-start m-8 justify-center gap-6 lg:w-screen">
	{#each testimonials as testimonial}
		<div
			class="rounded-[18px] border-2 border-sky-500 bg-gradient-to-br from-blue-900 via-blue-950 to-blue-900"
		>
			<div
				class="flex flex-col items-center justify-start gap-6 p-2 md:items-start lg:w-[397.33px] lg:items-center"
			>
				<div class="flex flex-col items-center justify-center gap-3 md:flex-row lg:flex-col">

					<div class="flex flex-col items-center justify-center md:items-start lg:items-center">
						<Header3>{testimonial.title1}</Header3>
						<Header4>{testimonial.title2}</Header4>
					</div>
				</div>
			</div>
		</div>
	{/each}
</div>
