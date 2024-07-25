<script lang="ts">
	import { onMount } from 'svelte';
	export let list = [''];

	let contentContainer: HTMLElement | null = null;

	onMount(() => {
		if (contentContainer) {
			contentContainer.scrollTop = contentContainer.scrollHeight;
		}
	});
</script>

<div bind:this={contentContainer} class="mx-auto h-48 w-10/12 overflow-auto">
	<ol class="custom-ol rounded-lg bg-gray-800 p-4 text-white">
		{#each list as line}
			<li>
				<span class="custom-li-content">{line}</span>
			</li>
		{/each}
	</ol>
</div>

<style>
	.custom-ol li {
		counter-increment: custom-counter;
	}
	.custom-ol li::before {
		content: counter(custom-counter);
		margin-right: 6px;
	}
	.custom-li-content {
		display: inline-block;
		vertical-align: top; /* Aligns content at the top */
	}
</style>
