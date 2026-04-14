"use client"; // required for hooks in Next.js app router

import React, { useEffect, useState } from "react";

const Test = () => {
    const [backendResponse, setBackendResponse] = useState(null);

    useEffect(() => {
        const backendUrl = `http://${process.env.NEXT_PUBLIC_BACKEND_IP}:${process.env.NEXT_PUBLIC_BACKEND_PORT}/ping`;

        fetch(backendUrl)
            .then((res) => res.json())
            .then((data) => setBackendResponse(data))
            .catch((err) => {
                console.error("Error fetching backend:", err);
                setBackendResponse({ message: "Failed to connect to backend" });
            });
    }, []);

    return (
        <div>
            <h1>This is TEST Path</h1>
            {backendResponse ? (
                <div>
                    <p>Data: {backendResponse.data}</p>
                    <p>Message: {backendResponse.message}</p>
                </div>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default Test;
