import { jwtDecode } from 'jwt-decode';

export const getUserId = () => {
    const token = localStorage.getItem('token');
    if (!token) {
        return null;
    }

    const decoded_token = jwtDecode(token);
    return decoded_token.user_id;
};

export const register = async (email, password, name) => {
    const response = await fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email,
            password,
            name
        }),
    });

    if (response.ok) {
        const data = await response.json();
        localStorage.setItem('token', data.token);
        return { success: true };
    } else {
        const error = await response.json();
        return { success: false, message: error.message };
    }
};


export const login = async (email, password) => {
    const response = await fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email,
            password,
        }),
    });

    if (response.ok) {
        const data = await response.json();
        localStorage.setItem('token', data.token);
        return { success: true };
    } else {
        const error = await response.json();
        return { success: false, message: error.message };
    }
};

export const setUserName = async (userId, name) => {
    const response = await fetch(`/user/${userId}/name`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            name,
        }),
    });

    return await response.json();
};

export const setUserBio = async (userId, bio) => {
    const response = await fetch(`/user/${userId}/bio`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            bio,
        }),
    });

    return await response.json();
};

export const getUserProfile = async (userId) => {
    const response = await fetch(`/user/${userId}`, {
        method: 'GET',
    });

    return await response.json();
};

export const getUserNotes = async (userId) => {
    const response = await fetch(`/user/${userId}/notes`, {
        method: 'GET',
    });

    return await response.json();
};

export const createNotebook = async (title, ownerId) => {
    const response = await fetch('/notebooks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            title,
            owner_id: ownerId,
        }),
    });

    return await response.json();
};

export const getNotebooks = async (userId) => {
    const response = await fetch(`/${userId}/notebooks`, {
        method: 'GET',
    });

    return await response.json();
};

export const getNotebook = async (notebookId) => {
    const response = await fetch(`/notebooks/${notebookId}`, {
        method: 'GET',
    });

    return await response.json();
};

export const renameNotebook = async (notebookId, newTitle) => {
    const response = await fetch(`/notebooks/${notebookId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            title: newTitle,
        }),
    });

    return await response.json();
};

export const deleteNotebook = async (notebookId) => {
    const response = await fetch(`/notebooks/${notebookId}`, {
        method: 'DELETE',
    });

    return await response.json();
};

export const getNotesFromNotebook = async (notebookId) => {
    const response = await fetch(`/notebooks/${notebookId}/notes`, {
        method: 'GET',
    });

    return await response.json();
};

export const addNoteToNotebook = async (notebookId, noteId) => {
    const response = await fetch(`/notebooks/${notebookId}/notes/${noteId}`, {
        method: 'POST',
    });

    return await response.json();
};

export const createNote = async (title) => {
    const response = await fetch('/notes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            title,
        }),
    });

    return await response.json();
};

export const getNote = async (noteId) => {
    const response = await fetch(`/notes/${noteId}`, {
        method: 'GET',
    });

    return await response.json();
};

export const deleteNote = async (noteId) => {
    const response = await fetch(`/notes/${noteId}`, {
        method: 'DELETE',
    });

    return await response.json();
};

export const saveNoteContent = async (noteId, content, editorId) => {
    const response = await fetch(`/notes/${noteId}/versions`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            content,
            editor_id: editorId,
        }),
    });

    return await response.json();
};

export const getNoteVersions = async (noteId) => {
    const response = await fetch(`/notes/${noteId}/versions`, {
        method: 'GET',
    });

    return await response.json();
};

export const getNoteVersionByDate = async (noteId, date) => {
    const response = await fetch(`/notes/${noteId}/versions/${date}`, {
        method: 'GET',
    });

    return await response.json();
};

export const getNoteOwners = async (noteId, currentUserId) => {
    const response = await fetch(`/notes/${noteId}/owners`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            current_user_id: currentUserId,
        }),
    });

    return await response.json();
};

export const addNoteOwner = async (noteId, userId) => {
    const response = await fetch(`/notes/${noteId}/owners/${userId}`, {
        method: 'POST',
    });

    return await response.json();
};



