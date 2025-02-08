import React, {useEffect, useState} from 'react';
import Link from 'next/link';

type Post = {
    id: number;
    title: string;
    content: string;
}

export async function getServerSideProps() {
    const res = await fetch('http://localhost:8000/posts');
    const posts: Post[] = await res.json();
    
    return {
        props: { posts }
    }
}

export default function Home({ posts }: { posts: Post[] }) {
    return (
        <div>
            <h1>게시글 목록!</h1>
            <ul>
                {posts.map(post => (
                    <li key={post.id}>
                    <Link href={`/posts/${post.id}`} key={post.id}>
                        {post.title}</Link>
                    </li>
                ))}
            </ul>
        </div>
    )
}