import {createSignal} from 'solid-js';

export function Notes(){
    const [notes, setNotes] = createSignal([]);
    const [selected, setSelected] = createSignal(null);
    const [title, setTitle] = createSignal('');
    const [body, setBody] = createSignal('');

    function newNote(){
        setSelected({id: null});
        setTitle('');
        setBody('');
    }

    async function openNote(id){
        const note = await get(`/notes/${id}`);
        setSelected(note);
        setTitle(note.title || '');
        setBody(note.body || '');
    }

    return (
        <section class='notes'>
            <p>This is where the notes will go.</p>
            <aside class='note-list'>
                <button class='new-note' onClick={newNote}>+</button>
                <For each={notes()}>
                    {(n) => (
                        <button class='note-item' onClick={() => openNote(n.id)}>
                            {n.title || 'untitled'}
                        </button>
                    )}
                </For>
            </aside>
        </section>
    );
}