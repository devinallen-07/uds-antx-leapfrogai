<script>
	import { Badge } from 'flowbite-svelte';
</script>

<div class="m-4 flex grid grid-cols-2 flex-wrap justify-center text-xl">
	<div class="grid grid-cols-1">
		<p>Transcription Time (s)</p>
		<div class="grid grid-cols-2 p-4 indent-10">
			<span>minimum</span>
			<Badge class="m-0.5 w-1/2" border>23.1</Badge>
			<span>maximum</span>
			<Badge class="m-0.5 w-1/2" border>23.1</Badge>
			<span>average</span>
			<Badge class="m-0.5 w-1/2" border>23.1</Badge>
		</div>
	</div>
	<div class="grid grid-cols-1">
		<p>Inferencing Time (s)</p>
		<div class="grid grid-cols-2 p-4 indent-10">
			<span>minimum</span>
			<Badge class="m-0.5 w-1/2" border>23.1</Badge>
			<span>maximum</span>
			<Badge class="m-0.5 w-1/2" border>23.1</Badge>
			<span>average</span>
			<Badge class="m-0.5 w-1/2" border>23.1</Badge>
		</div>
	</div>
</div>
