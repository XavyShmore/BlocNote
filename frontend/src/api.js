import { jwtDecode } from 'jwt-decode';

const API_URL = 'http://localhost:5000';

export const getUserId = () => {
    const token = localStorage.getItem('token');
    if (!token) {
        return null;
    }

    const decoded_token = jwtDecode(token);
    return decoded_token.user_id;
};

export const register = async (email, password, name) => {
    const response = await fetch(`${API_URL}/register`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "mode": "no-cors", "access-control-allow-origin": "*"
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
    const response = await fetch(`${API_URL}/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "mode": "no-cors", 
            "access-control-allow-origin": "*"
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
    const response = await fetch(`${API_URL}/user/${userId}/name`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            "mode": "no-cors", 
            "access-control-allow-origin": "*"
        },
        body: JSON.stringify({
            name,
        }),
    });

    return await response.json();
};

export const setUserBio = async (userId, bio) => {
    const response = await fetch(`${API_URL}/user/${userId}/bio`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            "mode": "no-cors", 
            "access-control-allow-origin": "*"
        },
        body: JSON.stringify({
            bio,
        }),
    });

    return await response.json();
};

export const getUserProfile = async (userId) => {
    const response = await fetch(`${API_URL}/user/${userId}`, {
        method: 'GET',
    });

    return await response.json();
};

export const getUserNotes = async (userId) => {
    const response = await fetch(`${API_URL}/user/${userId}/notes`, {
        method: 'GET',
    });

    return await response.json();
};

export const createNotebook = async (title, userId) => {
    const response = await fetch(`${API_URL}/${userId}/notebooks`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "mode": "no-cors", 
            "access-control-allow-origin": "*"
        },
        body: JSON.stringify({
            title,
        }),
    });

    return await response.json();
};


export const getNotebooks = async (userId) => {
    const response = await fetch(`${API_URL}/${userId}/notebooks`, {
        method: 'GET',
    });

    return await response.json();
};

export const getNotebook = async (notebookId) => {
    const response = await fetch(`${API_URL}/notebooks/${notebookId}`, {
        method: 'GET',
    });

    return await response.json();
};

export const renameNotebook = async (notebookId, newTitle) => {
    const response = await fetch(`${API_URL}/notebooks/${notebookId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            "mode": "no-cors", 
            "access-control-allow-origin": "*"
        },
        body: JSON.stringify({
            title: newTitle,
        }),
    });

    return await response.json();
};

export const deleteNotebook = async (notebookId) => {
    const response = await fetch(`${API_URL}/notebooks/${notebookId}`, {
        method: 'DELETE',
    });

    return await response.text().then(text => text ? JSON.parse(text) : {});
};

export const getNotesFromNotebook = async (notebookId) => {
    const response = await fetch(`${API_URL}/notebooks/${notebookId}/notes`, {
        method: 'GET',
    });

    return await response.json();
};

export const addNoteToNotebook = async (notebookId, noteId) => {
    const response = await fetch(`${API_URL}/notebooks/${notebookId}/notes/${noteId}`, {
        method: 'POST',
    });

    return await response.json();
};

export const createNote = async (title, userId) => {
    const response = await fetch(`${API_URL}/${userId}/notes`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "mode": "no-cors", 
            "access-control-allow-origin": "*"
        },
        body: JSON.stringify({
            title,
        }),
    });

    return await response.json();
};


export const getNote = async (noteId) => {
    const response = await fetch(`${API_URL}/notes/${noteId}`, {
        method: 'GET',
    });

    return await response.json();
};

export const deleteNote = async (noteId) => {
    const response = await fetch(`${API_URL}/notes/${noteId}`, {
        method: 'DELETE',
    });

    return await response;
};

export const setNoteTitle = async (noteId, title) => {
    const response = await fetch(`${API_URL}/notes/${noteId}/title`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            "mode": "no-cors", 
            "access-control-allow-origin": "*"
        },
        body: JSON.stringify({ title })
    });

    return await response.json();
};


export const saveNoteContent = async (noteId, content, userId) => {
    const response = await fetch(`${API_URL}/${userId}/notes/${noteId}/versions`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "mode": "no-cors", 
            "access-control-allow-origin": "*"
        },
        body: JSON.stringify({
            content,
        }),
    });

    return await response.json();
};

export const getNoteVersions = async (noteId) => {
    const response = await fetch(`${API_URL}/notes/${noteId}/versions`, {
        method: 'GET',
    });

    return await response.json();
};

export const getNoteVersionByDate = async (noteId, date) => {
    const formattedDate = new Date(date).toISOString();
    const response = await fetch(`${API_URL}/notes/${noteId}/versions/date`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            "mode": "no-cors", 
            "access-control-allow-origin": "*"
        },
        body: JSON.stringify({
            date: formattedDate
        })
    });

    return await response.json();
};

export const getNoteOwners = async (noteId, currentUserId) => {
    const response = await fetch(`${API_URL}/${currentUserId}/notes/${noteId}/owners`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            "mode": "no-cors", 
            "access-control-allow-origin": "*"
        },
    });

    return await response.json();
};

export const addNoteOwner = async (noteId, email) => {
    const response = await fetch(`${API_URL}/notes/${noteId}/owners`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "mode": "no-cors", 
            "access-control-allow-origin": "*"
        },
        body: JSON.stringify({ email })
    });

    return await response.json();
};


export const getRecentNotes = async (userId) => {
    const response = await fetch(`${API_URL}/${userId}/recent`, {
        method: 'GET',
    });

    return await response.json();
};


